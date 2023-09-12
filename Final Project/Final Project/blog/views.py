from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
import requests

from .models import Blog, Category, Tag, Comment
from .forms import CommentForm


def home(request):
    # Get the latest 6 blog posts for the carousel
    latest_posts = Blog.objects.filter(status='published').order_by('-created_at')[:6]

    # Get 3 featured posts (adjust this query as needed)
    featured = Blog.objects.filter(status='published', featured=True)[:3]

    # Create a dictionary to store the comment counts
    featured_posts = {}

    # Iterate over the featured posts
    for post in featured:
        # Get all of the comments for the post
        comments = Comment.objects.filter(blog=post, parent_comment=None)

        # Exclude the replies from the comments
        featured_posts[post] = comments.count()

    # Get 2 different categories (you can adjust this logic)
    categories = Category.objects.all()[:2]

    # Create a dictionary to hold the posts for each category
    category_posts = {}
    for category in categories:
        posts = Blog.objects.filter(categories=category)[:2]  # Change this to get more posts per category
        category_posts[category] = posts

    context = {
        'latest_posts': latest_posts,
        'featured_posts': featured_posts,
        'category_posts': category_posts,
    }

    return render(request, 'pages/home.html', context)


def blog_list(request):
    blogs = Blog.objects.all().filter(status='published')

    # Number of blogs to display per page
    blogs_per_page = 10  # You can adjust this as needed

    # Create a Paginator object
    paginator = Paginator(blogs, blogs_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page = paginator.get_page(page_number)

    context = {'page': page}
    return render(request, 'pages/blog.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = Comment.objects.filter(blog=blog, parent_comment=None)
    comment_count = comments.count()
    comment_form = CommentForm()

    # Get the next and previous blog posts
    next_post = Blog.objects.filter(status='published', created_at__gt=blog.created_at).order_by('created_at').first()
    previous_post = Blog.objects.filter(status='published', created_at__lt=blog.created_at).order_by('-created_at').first()

    if request.method == 'POST':
        # Check if it's a reply or a top-level comment
        if 'parent_comment' in request.POST:
            # If 'parent_comment_id' is in POST data, it's a reply
            parent_comment_id = request.POST['parent_comment']
            parent_comment = Comment.objects.get(id=parent_comment_id)
            comment_form = CommentForm(request.POST, initial={'parent_comment': parent_comment})
        else:
            # If 'parent_comment_id' is not in POST data, it's a top-level comment
            comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.author = request.user
            new_comment.save()

            # Redirect back to the same page (blog_detail) after comment submission
            return redirect('post', slug=slug)

    context = {
        'blog': blog,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
        'next_post': next_post,
        'previous_post': previous_post,
    }
    return render(request, 'pages/single.html', context)


def blog_by_category(request, category):
    category = get_object_or_404(Category, name=category)
    blogs = Blog.objects.filter(categories=category)

    # Number of blogs to display per page
    blogs_per_page = 10  # You can adjust this as needed

    # Create a Paginator object
    paginator = Paginator(blogs, blogs_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page = paginator.get_page(page_number)

    context = {'category': category, 'page': page}
    return render(request, 'pages/category.html', context)


def blog_by_tag(request, tag):
    tag = get_object_or_404(Tag, name=tag)
    blogs = Blog.objects.filter(tags=tag)

    # Number of blogs to display per page
    blogs_per_page = 10  # You can adjust this as needed

    # Create a Paginator object
    paginator = Paginator(blogs, blogs_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page = paginator.get_page(page_number)

    context = {'tag': tag, 'page': page}
    return render(request, 'pages/tag.html', context)


def blog_search(request):
    if request.method == 'POST':
        # Get the search query from the form data
        query = request.POST.get('query', '')

        # Store the search query in the session
        request.session['search_query'] = query

    # Get the search query from the session
    query = request.session.get('search_query', '')

    # Filter blogs based on the search query (you can customize this)
    blogs = Blog.objects.filter(title__icontains=query, status='published')

    # Number of blogs to display per page
    blogs_per_page = 10  # You can adjust this as needed

    # Create a Paginator object
    paginator = Paginator(blogs, blogs_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page = paginator.get_page(page_number)

    context = {'query': query, 'page': page}

    return render(request, 'pages/search.html', context)


def about(request):
    return render(request, 'pages/about.html', {})


def contact(request):
    message = None

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Prepare the data for the Email.js request
        emailjs_data = {
            'service_id': settings.EMAILJS_SERVICE_ID,
            'template_id': settings.EMAILJS_TEMPLATE_ID,
            'user_id': settings.EMAILJS_USER_ID,
            'accessToken': settings.EMAILJS_ACCESS_TOKEN,
            'template_params': {
                'from_name': name,
                'to_name': settings.EMAILJS_TO_NAME,
                'reply_to': email,
                'message': message,
            }
        }

        # Send the email using Email.js
        response = requests.post(
            'https://api.emailjs.com/api/v1.0/email/send',
            json=emailjs_data,
            headers={'Content-Type': 'application/json',},
        )

        if response.status_code == 200:
            message = 'Email sent successfully!'
        else:
            message = 'Email sending failed.'

    context = {'message': message}

    return render(request, 'pages/contact.html', context)


def custom_404_error_view(request, exception):
    return render(request, 'pages/404.html', status=404)
