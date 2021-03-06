from setuptools import setup, find_packages
import shutil
import sys
import os
import os.path


# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


if 'install' in sys.argv:
    try:
        import django
    except ImportError:
        pass
    else:
        if django.VERSION >= (1,7):
            shutil.rmtree(os.path.join(os.path.dirname(__file__),
                                       'cities_light', 'migrations'))


setup(
    name='django-cities-light',
    version='2.1.13',
    description='Simple alternative to django-cities',
    author='James Pic',
    author_email='jamespic@gmail.com',
    url='https://github.com/yourlabs/django-cities-light',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.rst'),
    license = 'MIT',
    keywords = 'django cities countries postal codes',
    install_requires=[
        'six',
        'unidecode>=0.04.13',
        'django_autoslug',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

