import setuptools

with open("README.md", "r") as read_obj:
    long_description = read_obj.read()

setuptools.setup(
    name="wsu",
    version="0.0.1",
    author="Brett Vanderwerff",
    author_email="cougpy@gmail.com",
    description="A small example package",
    long_description=long_description,
    url="https://github.com/wsucougpy/package-demo",
    packages=setuptools.find_packages(),
    install_requires=[
       'numpy'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
