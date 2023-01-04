from setuptools import setup
import re
import os
import sys

setup(
    name="auto-device",
    version="0.0.0",
    python_requires=">3.7.0",
    author="Michael E. Vinyard - Harvard University - Massachussetts General Hospital - Broad Institute of MIT and Harvard",
    author_email="mvinyard@broadinstitute.org",
    url="https://github.com/mvinyard/sc-neural-diffeqs",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="",
    packages=setuptools.find_packages(),
    install_requires=[
        "torch>=1.12.0",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="MIT",
)
