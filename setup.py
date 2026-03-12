"""Setup script"""
from setuptools import setup, find_packages

setup(
    name="vscode-toolkit",
    version="0.1.0",
    description="Vscode toolkit and utilities",
    author="Developer",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        # Add dependencies here
    ],
    entry_points={
        "console_scripts": [
            "vscode-toolkit=src.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
)
