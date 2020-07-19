import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylogapp-spohess",
    version="0.0.1",
    author="Sergio Hess",
    author_email="hess.sergio@gmail.com",
    description="Package to append app menssages to an log file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spohess/pylogapp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
