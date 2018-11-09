# Package Demo



## Why package a project? 

Packaging a project can make the project easier to share with others. Packaging can also provide a hierarchical template
for organizing the logical components of a program, which can help make the program easier to understand and extend.

## Modules

To understand a python package we first must understand what a python module is and how they are imported.

Python modules are files with a `.py` extension that contain python code.

In the top level directory of our repository we have a module called `mod.py`, which contains a simple function for 
printing the string "forty-two". 

`mod.py` :
```python
def forty_two():
    print('forty two')
```

If we start an interactive session of python in the top level directory of our repository we can import `mod.py` and 
access functions within the module using a dot notation.

```commandline
$python3
```
```commandline
>>>import mod
>>>mod.forty_two()
forty two
```

## Packages

Packages are directories that contain an `__init__.py` file, which allows us to import an entire directory as if it was a module.
After importing a package, we can access submodules (modules within the package) and functions within submodules by 
using a dot notation similar to what we did with `mod.py`. 

##### Package organization tips:

* Functions within submodules should do one thing only and do it well. 

* Submodules typically contain functions that are related. 

* Submodules should not be too dependent on each other (ideally not at all).

* Packages should contain submodules that all contribute to the completion of some common, broad task.  


Lets take a look at the contents of the `wsu` directory, a pretend package that scrapes sites and
visualizes the results:

```
wsu/
├──scraper.py
├──visual.py
└──__init__.py
```


`scraper.py` contains one function that scrapes a site:
```python

def scrape():
    print('Scraping site')
```

`visual.py` contains one function that plots some results:

```python

def plot():
    print('Making bar graph')

```

`__init__.py` is a special Python file the defines `wsu` as a package. Without `__init__.py` Python will not recognize
`wsu` as something that it can import. `__init__.py` can be left empty, but sometimes people will import a few core 
classes/functions within `__init__.py` to make these items more accessible for the user.
 Also any top-level code within `__init__.py`  (outside of a function etc.) will be run as soon as the package
is imported. This can be used to initialize things like configuration values or logging.

`__init__.py`:
```python
from .scraper import scrape
from .visual import plot
```

By opening an interactive session of Python in the top level repository directory we can import `wsu` and access content
within it using a dot notation similar to what we did when importing the example module.

```commandline
$python3
```
```commandline
>>>import wsu
>>>wsu.scrape()
Scraping site

>>>wsu.plot()
Making bar graph

```

Note that if we had left `__init__.py` empty the user would need to do something like this to access the same functions:

```commandline
>>>from wsu import scraper
>>>scraper.scrape()
Scraping site

```

## The Python Package Index

 The Python Package Index (PyPI, https://pypi.org/), is a large online repository for Python packages. 
 Anyone who wants to pull a package from PyPI to use on their personal machine can do so easily with the 
 Python package management system `pip`. At the time of writing this, there are 157,000 packages on PyPI. The rest of
 this tutorial is going to focus on how to prepare a package for uploading to PyPI using our `wsu` package as an example. 
 
 ## The "non-package" files
 
 Lets take a look at the contents of the repository outside of the `wsu` directory.
```
.
│
├──wsu/     
│   ├──scraper.py   
│   ├──visual.py
│   └──__init__.py
├──LICENSE
├──README.rst
└──setup.py
 
```

#### LICENSE.txt

Licenses are optional for PyPI, but good to include
with our work because if anyone comes across the project and wants to use some of the code 
they can get a feel for what they can and cannot do without needing to contact us and ask. 
No one wants to be accused of passing off someone else's code as their own. I picked the MIT license because it is short and easy to understand.

`LICENSE.txt`:

```text
MIT License

Copyright (c) 2018 brettvanderwerff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
#### README.md

A readme file is also technically optional for PyPI, but a very good thing to include. Our readme is a markdown file 
that does not have much in it, but
you can see an example [readme template](https://github.com/dbader/readme-template) for inspiration on what a 
full fledged project might have.

`README.md`:

```markdown
# wsu

A tutorial on uploading a package to the Python Package Index.

## Usage example

```commandline
>>>import wsu
>>>wsu.scrape()
Scraping site

>>>wsu.plot()
Making bar graph

```

#### setup.py

setup.py is required for our upload process. It establishes mostly meta-data but also some information about what
packages we want to
distribute and what their dependencies are.

`setup.py`:

```python
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
    url="https://github.com/wsucougpy/package_demo",
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

```

There is a lot going on in `setup.py`, but we can look at it piece by piece.

1. First we import setuptools, which is a tool that facilitates the preparation of Python packages for distribution.

2. Then we open the `README.md` file and store it's contents in a variable called `long_description`.

3. setuptools has a setup function that runs the setup. To the setup function we pass the following arguments: 

* name: The name of our package :)
* version: Often follows the format ["major.minor.micro"](https://www.python.org/dev/peps/pep-0440/)
* author: My name
* author_email: My email
* description: Just a short blurb about what the package does. People will see this description alongside the project 
name when looking through PyPI search results. 
* long description: A long blurb about what the project does, it is common to set this equal to a variable containing 
the entire README file.
* url: A url for the source code repository, in our case a repository hosted on Github.
* packages: We set this equal to `setuptools.find_packages()`, which will walk through the project directory 
and return a list of all directories containing an `__init__.py` file.
* install_requires: This is a list of dependencies. When someone installs our package from PyPI, an attempt will also be made to 
install these dependencies. 
* classifiers: [Classifiers](https://pypi.org/pypi?%3Aaction=list_classifiers) will end up being tags on PyPI that 
will help people search for the project. 

## Uploading a package to PyPI

1. Lets make sure setuptools is installed. 

```commandline
$pip3 install -U setuptools 

```

This command installs the python package setuptools. The U flag indicates that setuptools will be upgraded to the 
most recent version if one is available. 

2. Run the setup.py script to create the distribution of our package. 

```commandline
$python3 setup.py sdist
```

This command creates a directory `dist/` in our top level directory. A gzipped file including our package and 
some meta-data is written in this `dist` directory. 

3. We need to make an account on [TestPyPI](https://test.pypi.org/account/register/). This is a test instance of the real PyPI 
that lets us test our uploading process without affecting the real PyPI. Its important to remember what username and
password was used in the registration process (we will be prompted for it later). 
It is also important to confirm the email address that was registered. Without confirming the email address uploading
to TestPyPI will fail.


4. Lets make sure twine is installed

```commandline
$pip3 install -U twine
```
Twine is a tool for securely interfacing with PyPI/TestPyPI and uploading our package.

5. After installing twine, we will use it to upload our package by using the following command 

```commandline
$twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

This command indicates that everything in the `dist` directory that we generated by running our `setup.py` file is to be
uploaded using the url for TestPyPI. Assuming twine is able to form a connection, we will be prompted to enter 
our TestPyPI username and password. Failing to confirm our email address with TestPyPI will result in an error at this
step.

Once the upload is successful, we should be able to see the project online here: https://test.pypi.org/project/wsu/

6. We can test installing our package from TestPyPI using pip. 

```commandline
$pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple wsu
```

The `--index-url` flag indicates that we want to pull our package from TestPyPI. The `--extra-url` flag  
indicates that we want to pull any of our project's dependencies that are not available on TestPyPI from the real PyPI.
In our case, this installs the numpy dependency by pulling numpy from the real PyPI.

7. If we want confirmation that everything worked, we can open an interactive session of python anywhere and import `wsu`. This should work even if we delete the `wsu` directory in the demo repository.

```commandline
$python3
```

```commandline
>>>import wsu
>>>wsu.scrape()
Scraping site
```

8. Uploading to the real PyPI is really straight forward, we would just go back to the top level directory of the repository, 
and upload the package to PyPI with the following command:

```commandline
$twine upload dist/*
```

We are not going to do this, because there is really no sense in cluttering the real PyPI with our demo package.

In summary Python packages can offer a good organizational template for developing projects.
Also, packages can make sharing a project with others easier.  

## References

1. https://packaging.python.org/tutorials/packaging-projects/
2. https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
3. https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
4. http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
5. https://packaging.python.org/guides/using-testpypi/
6. https://docs.python-guide.org/writing/structure/








 
 
 









