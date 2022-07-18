"""
    Finix API

    The version of the OpenAPI document: 2022-02-01
    Contact: support@finixpayments.com
"""


import os
from codecs import open
from setuptools import setup, find_packages  # noqa: H301

NAME = "finix"
VERSION = "3.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

current_path = os.path.abspath(os.path.dirname(__file__))
os.chdir(current_path)
with open(os.path.join(current_path, "LONG_DESCRIPTION.rst"), "r", encoding="utf-8") as f_ld:
    long_description_file = f_ld.read()

setup(
    name=NAME,
    version=VERSION,
    description="Finix API client library",
    author="Finix",
    author_email="support@finixpayments.com",
    url="https://github.com/finix-payments/finix-python",
    keywords=["Payment", "Finix API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache",
    long_description=long_description_file,
    long_description_content_type="text/x-rst",
    project_urls={
        "Source Code": "https://github.com/finix-payments/finix-python",
        "Bug Tracker": "https://github.com/finix-payments/finix-python/issues",
        "Changes": "https://github.com/finix-payments/finix-python/blob/main/CHANGELOG.md",
        "Documentation": "https://www.finix.com/docs",
    },
)
