# setup.py
from setuptools import setup, find_packages

setup(
    name="calculatorLab",
    version="0.1",
    packages=find_packages(),
    # py_modules=["main", "operations", "utils"],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'calculator = calculatorLab.main:main'
        ]
    },
    description="Simple calculator with logging and testing",
)