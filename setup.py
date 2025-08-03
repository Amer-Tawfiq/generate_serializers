from setuptools import setup, find_packages

setup(
    name='generate_serializers',
    version='0.1.0',
    description='A utility to auto-generate Django REST Framework serializers for all models in specified apps',
    author='ْAmer Al-Jabri',
    author_email='amerprogrammer85@gmail.com',
    url='https://github.com/Amer-Tawfiq/generate_serializers.git',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'djangorestframework',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
