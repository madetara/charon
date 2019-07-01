from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='dk.charon',
    author="Danil Kabanov",
    author_email="madetara@yandex.com",
    description="Tool for managing telegram chats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madetara/charon",
    version='0.1',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities"
    ],
    install_requires=[
        "telethon",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "charon=src.main:charon"
        ]
    }
)
