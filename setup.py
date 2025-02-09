from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f: # For long description in PyPi
    long_description = f.read()

setup(
    name="qr_generator",  # Your package name (must be unique on PyPI if you plan to publish)
    version="0.1.1",  # Initial version
    description="A package for generating QR codes with embedded images.",
    long_description=long_description, # Long description from README
    long_description_content_type="text/markdown", # Important for PyPi
    author="Uri Danan",
    author_email="uridanan@gmail.com",
    packages=find_packages(),  # Automatically find packages and subpackages
    install_requires=[  # List of dependencies
        "qrcode",
        "Pillow",
    ],
    classifiers=[ # For PyPi
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # Example license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7', # Minimum Python version
)