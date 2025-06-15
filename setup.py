# setup.py
from setuptools import setup, find_packages

setup(
    name="calculatorlab",
    version="0.1",
    packages=find_packages(),
    py_modules=["main", "operations", "utils"],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'calculator = main:main'
        ]
    },
    description="Simple calculator with logging and testing",
)