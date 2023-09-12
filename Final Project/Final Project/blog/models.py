from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from readtime import of_html

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Blog(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="blog/%Y/%m/%d/", default="avatar.png", null=True, blank=True)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    read_time = models.CharField(max_length=20, default="0 mins read", editable=False)
    featured = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft'
    )

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ("-created_at",)
        unique_together = ('title', 'slug')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.content:  # Calculate read time only when creating a new post or updating a post
            read_time = of_html(self.content)
            self.read_time = read_time

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', args=[str(self.slug)])

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Comment by {self.author.name} on {self.blog.title}'

    def children(self):
        return Comment.objects.filter(parent_comment=self)

    def parent(self):
        return self.parent_comment  # Return the parent comment, not the Comment object

    @property
    def is_parent(self):
        return self.parent_comment is None
