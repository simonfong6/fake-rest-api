from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="template-python-flask",
    version="0.0.1",
    author="Simon Fong",
    author_email="simonfong6@gmail.com",
    description="A package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simonfong6/template-python-flask",
    packages=find_packages(),
    install_requires=[
        'flask >= 1.1.1',
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
