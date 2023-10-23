from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="niyofetch",
    version="1.0.0",
    description="Embrace the GigaChad within you - Show off your system stats like a pro.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/r4mbhardwaj/niyofetch",
    author="r4mbhardwaj",
    author_email="r4mbhardwaj@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "niyofetch=niyofetch.niyofetch:run",
        ],
    },
)
