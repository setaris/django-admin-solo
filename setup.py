import sys

from setuptools import setup, find_packages

from admin import __version__

install_requires = [
    'django >= 1.5',
]

setup(
    name = "django-admin-solo",
    version = __version__,
    description = "Just Django admin with some refactoring to make it DRYer."
    url = "https://github.com/setaris/django-admin",
    author = "Setaris",
    author_email = "support@setaris.com",
    packages = find_packages(),
    install_requires = install_requires,
)
