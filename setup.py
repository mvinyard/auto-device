import setuptools
import re
import os
import sys

setuptools.setup(
    name="autodevice",
    version="0.0.2",
    python_requires=">3.7.0",
    author="Michael E. Vinyard - Harvard University - Massachussetts General Hospital - Broad Institute of MIT and Harvard",
    author_email="mvinyard@broadinstitute.org",
    url="https://github.com/mvinyard/autodevice",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="Automatically assign available hardware on the fly, in-line with PyTorch code.",
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
