"""
Setup script for pdfpg2img package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pdfpage2image",
    version="1.0.0",
    author="InnoVoltive",
    author_email="innovoltive@gmail.com",
    description="A simple Python utility to convert PDF pages to images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/innovoltive/pdfpage2image",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.19.0",
        "opencv-python>=4.5.0",
        "PyMuPDF>=1.18.0",
    ],
    keywords="pdf image converter pages extract",
    project_urls={
        "Bug Reports": "https://github.com/innovoltive/pdfpg2img/issues",
        "Source": "https://github.com/innovoltive/pdfpg2img",
    },
) 