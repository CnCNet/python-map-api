from kirovy.settings._base import *

TESTING_API_USERNAME = get_env_var("TESTING_API_USERNAME", "seth@brotherhood.nod")
TESTING_API_PASSWORD = get_env_var("TESTING_API_PASSWORD", "ripbozo1")
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env_var("POSTGRES_DB"),
        "USER": get_env_var("POSTGRES_USER"),
        "PASSWORD": get_env_var("POSTGRES_PASSWORD"),
        "HOST": get_env_var("POSTGRES_TEST_HOST", "localhost"),
        "PORT": get_env_var("POSTGRES_PORT"),
    }
}

# MEDIA_ROOT gets modified in common_fixtures.py in the tmp_media_root fixture.
