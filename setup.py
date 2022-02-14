import os
import re
import codecs
from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-dynaconf',
    version=find_version("dynaconf", "__init__.py"),
    url="https://github.com/mhsiddiqui/django-dynaconf",
    description='Dynamic Configuration for your Django project',
    long_description=read('README.rst'),
    author='Muhammad Hassan Siddiqui',
    author_email='mhassan.eeng@gmail.com',
    license='MIT',
    keywords='django dynamic-configuration dynamic-settings django-settings-from-admin'.split(),
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=2.7',
    extras_require={
        'django': ['Django>1.10']
    },
    # entry_points={
    #     'pytest11': [
    #         'pytest-django-constance = constance.test.pytest',
    #     ],
    # },
)