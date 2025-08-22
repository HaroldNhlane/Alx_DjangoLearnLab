"""
Django settings for social_media_api project.
...
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Production Settings ---

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)axaf)(32!_r@cu&i%7hrqi3$gure+*arapi9yk*3!!&7$*tbe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Add your production domain name(s) here.
# Example: ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
ALLOWED_HOSTS = ['haroldnhlane.icu']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',

    # Your apps
    'accounts',
    'posts',
    'notifications',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'social_media_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'social_media_api.wsgi.application'


# Database - Configured for MySQL
# You will need to install mysqlclient: pip install mysqlclient
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'social_app',
        'USER': 'your_username',  # Replace with your MySQL username
        'PASSWORD': 'your_password',  # Replace with your MySQL password
        'HOST': 'localhost',  # Or the host of your MySQL server
        'PORT': '3306',
    }
}


# Password validation
# ...

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# ...

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# In production, you'll need to use a storage solution like AWS S3.
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# ...

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Add this line to your settings.py to specify the custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    # ... any other REST framework settings you might have
}

# --- Added for Production Security ---

# Redirects all HTTP traffic to HTTPS.
# Requires your hosting provider to handle SSL.

# SECURITY HEADERS
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True # Add this line
# ...

# Prevents the browser from trying to guess content types.
SECURE_CONTENT_TYPE_NOSNIFF = True

# Prevents browsers from loading pages with mixed content.
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Use `X_FRAME_OPTIONS` middleware to prevent clickjacking.
# The `XFrameOptionsMiddleware` is already in your MIDDLEWARE list.
# You can uncomment the line below if needed, but the middleware does this for you.
# X_FRAME_OPTIONS = 'DENY'