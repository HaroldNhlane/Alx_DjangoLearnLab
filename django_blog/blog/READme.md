
# Django Authentication System Documentation
This document outlines the setup and functionality of the user authentication system for your Django blog project.

## 1. File Structure
Place the built files in the following structure within your Django 'blog' app:
```
your_project/
  ├── blog/
  │   ├── templates/
  │   │   └── blog/
  │   │       ├── base.html
  │   │       ├── register.html
  │   │       ├── login.html
  │   │       ├── logout.html
  │   │       └── profile.html
  │   ├── forms.py
  │   ├── views.py
  │   └── urls.py
  └── your_project/
      ├── urls.py
      └── settings.py
```
## 2. Setup and Configuration
### a. Update settings.py
Make sure your 'blog' app is in `INSTALLED_APPS`. Then, add the following lines to the end of your `your_project/settings.py` file.
```python
# In your_project/settings.py
LOGIN_REDIRECT_URL = 'blog-home'  # CHANGE 'blog-home' to your homepage URL name
LOGIN_URL = 'login'
```
### b. Include App URLs in Project URLs
In your main `your_project/urls.py`, include the URLs from your blog app.
```python
# In your_project/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), // This includes all URLs from blog/urls.py
]
```
### c. Run Migrations
Django's auth system needs database tables. Run migrations to create them.
```bash
python manage.py makemigrations
python manage.py migrate
```
## 3. Functionality Explained
- **Registration (`/register/`):** New users can sign up with a username, email, and password.
- **Login (`/login/`):** Uses Django's built-in `LoginView`.
- **Logout (`/logout/`):** Uses Django's built-in `LogoutView`.
- **Profile (`/profile/`):** Authenticated users can view and update their username and email.

## 4. Security
- **CSRF Protection:** All forms use the `{% csrf_token %}` tag.
- **Password Hashing:** Django automatically handles secure password hashing.
- **Protected Views:** The profile page uses the `@login_required` decorator.

## 5. How to Test
1.  **Run Server:** `python manage.py runserver`
2.  **Register:** Navigate to `http://127.0.0.1:8000/register/` and create an account.
3.  **Login:** Log in with your new credentials.
4.  **Profile:** Navigate to the "Profile" link and update your info.
5.  **Logout:** Click the "Logout" link.
6.  **Test Protection:** Try to access `/profile/` after logging out. You should be redirected to the login page.
    