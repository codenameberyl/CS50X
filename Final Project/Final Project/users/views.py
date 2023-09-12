from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, RegistrationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)

                    # Get the 'next' parameter from the POST data
                    next_url = request.POST.get('next', '')

                    # Redirect to the URL specified in 'next', or to the home page if not provided
                    return redirect(next_url or 'home')
                else:
                    messages.error(request, 'Invalid email or password.')
        else:
            form = LoginForm()

    return render(request, 'pages/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)  # Create user instance but don't save to the database yet
                user.set_password(form.cleaned_data['password'])  # Hash the password
                user.save()  # Save the user with the hashed password
                login(request, user)
                messages.success(request, 'Registration successful.')
                # Get the 'next' parameter from the POST data
                next_url = request.POST.get('next', '')

                # Redirect to the URL specified in 'next', or to the home page if not provided
                return redirect(next_url or 'home')
        else:
            form = RegistrationForm()

    return render(request, 'pages/register.html', {'form': form})
