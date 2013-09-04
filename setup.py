import sys

from setuptools import setup, find_packages

install_requires = [
    'django >= 1.5',
]

setup(
    name = "django-admin-solo",
    version = '1.5.3.1',
    description = "Just Django admin with some refactoring to make it DRYer.",
    url = "https://github.com/setaris/django-admin-solo",
    author = "Setaris",
    author_email = "support@setaris.com",
    packages = find_packages(),
    install_requires = install_requires,
)
