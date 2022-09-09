from setuptools import setup, find_packages  # noqa: H301

NAME = "python-liquid"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
]

setup(
    name=NAME,
    version=VERSION,
    description="Fork of Python Liquid",
    author="",
    author_email="",
    url="",
    keywords=[""],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=""
)
