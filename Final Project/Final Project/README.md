# Ìròyìn - A Django Blogging Web Application

Ìròyìn is a feature-rich Django-based blogging web application designed for bloggers and writers. It offers a clean and user-friendly interface for creating, managing, and sharing blog posts. This README.md file provides an overview of the project structure, features, and how to set it up for your use.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Creating an Admin User](#creating-an-admin-user)
  - [Starting the Development Server](#starting-the-development-server)
  - [Video Demo](#video-demo)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features

Ìròyìn is a powerful Django blogging platform that comes with a wide range of features, including:

- User Registration and Authentication:
  - Users can create accounts and log in.
  - Registration includes fields for name, email, and password.
- User Profile:
  - Users have profiles with avatars and bios.
- Blog Posts:
  - Users can create, edit, and delete blog posts.
  - Rich text editing with CKEditor.
  - Posts include titles, content, categories, and tags.
  - Posts have slugs for SEO-friendly URLs.
  - Posts have read time estimates.
- Categories and Tags:
  - Organize posts into categories and tags.
- Comments:
  - Users can comment on blog posts.
  - Comments can have replies.
- Search:
  - Search for blog posts.
- User Dashboard:
  - Users can view and manage their own posts.
- Admin Dashboard:
  - Powerful admin panel with Jazzmin for easy content management.
- Static Files:
  - Easily serve static files such as CSS, JavaScript, and images.
- Contact Form:
  - Users can send messages to the site owner via a contact form.
- Google reCAPTCHA:
  - Protects against spam and abuse in forms.
- Email Notifications:
  - Users receive email notifications for various actions (e.g., new comment, registration).
- Responsive Design:
  - Works well on desktop and mobile devices.

## Project Structure

Ìròyìn follows a typical Django project structure. Here are the key directories and files:

- `iroyin/`: The project's root directory.
  - `settings.py`: Django project settings.
  - `urls.py`: Main URL configuration.
- `users/`: App for user-related functionality.
  - `models.py`: Defines the custom user model.
  - `views.py`: Views for user registration, login, and logout.
  - `urls.py`: Users Main URL configuration.
  - `forms.py`: User authentication and registration forms.
- `blog/`: App for blog-related functionality.
  - `models.py`: Defines blog post, category, tag, and comment models.
  - `views.py`: Views for blog posts, categories, tags, and comments.
  - `urls.py`: Blog Main URL configuration.
  - `forms.py`: Forms for creating and managing blog posts and comments.
- `templates/`: HTML templates for the website.
- `static/`: Static files (CSS, JavaScript, images).
- `.env`: Example environment variables file.
- `manage.py`: Django's command-line utility for managing the project.
- `README.md`: Project's documentation file.
- `requirements.txt`: Project's dependencies file.

## Getting Started

Follow these instructions to set up and run Ìròyìn on your local machine.

### Prerequisites

Make sure you have the following software installed:

- Python (>=3.8)
- pip
- virtualenv (optional but recommended)

### Installation

1. Clone the Ìròyìn repository to your local machine:

   ```bash
   git clone https://github.com/codenameberyl/CS50X.git
   ```

2. Change to the project directory:

   ```bash
   cd "Final Project"/"Final Project"
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **Linux/macOS**:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running Ìròyìn, you need to configure some settings. Create a `.env` file in the project root directory (you can copy the `.env.example` file and modify it).

Example `.env` file:

```dotenv
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
RECAPTCHA_PUBLIC_KEY=your-recaptcha-public-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-private-key
EMAILJS_SERVICE_ID=your-emailjs-service-id
EMAILJS_TEMPLATE_ID=your-emailjs-template-id
EMAILJS_USER_ID=your-emailjs-user-id
EMAILJS_ACCESS_TOKEN=your-emailjs-access-token
EMAILJS_TO_NAME=your-emailjs-recipient-name
```

Note:
- Generate a new Django secret key for `SECRET_KEY`.
- Obtain reCAPTCHA keys from the [reCAPTCHA website](https://www.google.com/recaptcha) for `RECAPTCHA_PUBLIC_KEY` and `RECAPTCHA_PRIVATE_KEY`.
- For email functionality, sign up for an account at [Email.js](https://www.emailjs.com/) and obtain the service ID, template ID, user ID, and access token.

## Usage

### Creating an Admin User

To create an admin user for accessing the admin panel, run the following command:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter a username, email, and password.

### Starting the Development Server

To start the development server, run:

### Video Demo

Check out the video demonstration of Ìròyìn - A Django Blogging Web Application:

[![Ìròyìn Demo](https://i.imgur.com/JCqGZC5.png)](https://youtu.be/XXHqEb16mCk)

Click the image above or [here](https://youtu.be/XXHqEb16mCk) to watch the demo video.

```bash
python manage.py runserver
```

You can access the site at [http://localhost:8000/](http://localhost:8000/).

![Home | Ìròyìn](https://i.imgur.com/iZHljox.png)

![Blog | Ìròyìn](https://i.imgur.com/Ak6GAab.png)

Access the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/) and log in with the admin user you created.

![Admin Dashboard | Ìròyìn](https://i.imgur.com/phtRB2G.png)

![Admin Blogs | Ìròyìn](https://i.imgur.com/xCjrGLG.png)

![Admin Add Blog | Ìròyìn](https://i.imgur.com/L6Z0WLf.png)

## Customization

Ìròyìn is highly customizable. Here are some ways you can customize it:

- **Styling**: Modify the CSS files in the `static` directory to change the look and feel of the site.

- **Templates**: Customize the HTML templates in the `templates` directory to change the layout and design of pages.

- **Models**: Extend or modify the Django models in the `blog/models.py` and `users/models.py` files to add new features or data fields.

- **Views**: Customize the views in the `blog/views.py` and `users/views.py` files to change the behavior of the site.

- **Jazzmin**: Modify the `JAZZMIN_SETTINGS` and `JAZZMIN_UI_TWEAKS` dictionaries in `settings.py` to customize the appearance and functionality of the admin panel.

Remember to run `python manage.py makemigrations` and `python manage.py migrate` after making changes to models.

## Important Links

- HTML Template: [untree.co](https://untree.co/free-templates/story-free-bootstrap-template-for-personal-blog-and-portfolio/)
- EmailJS: [emailjs](https://www.emailjs.com/)
- EmailJS API: [emailjs api](https://www.emailjs.com/docs/rest-api/send/)
- Random User Generator: [randomuser.me](https://randomuser.me/)
- Unsplash (for images): [unsplash.com](https://unsplash.com/)

## Contributing

Contributions are welcome! If you'd like to contribute to Ìròyìn or if you find any bugs or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.