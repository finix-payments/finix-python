"""
    Finix API

    The version of the OpenAPI document: 2022-02-01
    Contact: support@finixpayments.com
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "finix"
VERSION = "2.0.0"
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

setup(
    name=NAME,
    version=VERSION,
    description="Finix API client library",
    author="Finix",
    author_email="support@finixpayments.com",
    url="https://github.com/finix-payments/finix-python",
    keywords=["OpenAPI", "Finix API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    The Python SDK for Finix API.
    """
)
