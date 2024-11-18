from setuptools import setup, find_packages

setup(
    name="py_script_exec",
    version="1.2.0",
    description="A cross-platform Python script runner.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="jon429r",
    author_email="jonathanday088@gmail.com",
    url="https://github.com/jon429r/py_script_exec",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
