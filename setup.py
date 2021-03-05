import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="enceladus",
    version="0.0.2",
    description="A terminal toolkit by your side!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/doublevcodes/Enceladus.py",
    author="doublevcodes",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["enceladus"],
    include_package_data=True,
)
