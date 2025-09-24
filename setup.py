from setuptools import setup, find_packages

setup(
    name="KadoMatsu",
    version="0.0.0.0",
    install_requires=[
        "JPype1",
    ],
    include_package_data=True,
    packages=find_packages()
)
