from setuptools import setup

setup(
    name='charon',
    version='0.1',
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
