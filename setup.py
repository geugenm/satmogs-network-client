from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).resolve().parent

with (here / 'readme.md').open(encoding='utf-8') as readme:
    long_description = readme.read()

def load_requirements(file_name):
    with (here / file_name).open(encoding='utf-8') as f:
        return f.read().splitlines()

setup(
    version="0.1.0",
    name="satnogs-network-client-api",
    description="A Python client for interacting with the SATNOGS Network API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    author="evgeniy.gleba",
    install_requires=load_requirements('requirements.txt'),
    python_requires='>=3.6',
    extras_require={
        "test": ["pytest"],
        "dev": ["black", "flake8"],
    },
    packages=find_packages(exclude=["tests", "docs"]),
    keywords="satnogs telemetry satellite archive data network download",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
