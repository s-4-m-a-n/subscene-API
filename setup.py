from setuptools import setup

def readme():
    with open("README.md", "r") as fh:
        README = fh.read()
    return README
setup(
    name="subscene-API", 
    version="1.0",
    author="Suman Dhakal",
    author_email="dhakalsumn739@gmail.com",
    description="python3 subscene api wrapper",
    keywords ="pypi packages subscene api wrapper subtitle downloader package python3",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    License ="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages = ["subscene-API"],
    install_requires=requirements,
    entry_points = {
        "console_scripts":[
            "subscene_API = subscene-API.cli:main",
        ]
    }
)