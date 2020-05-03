import setuptools


def readme():
    with open("README.md", "r",encoding='utf-8') as fh:
        README = fh.read()
    return README


setuptools.setup(
    name="subsceneAPI", 
    version="0.2",
    author="Suman Dhakal",
    author_email="dhakalsumn739@gmail.com",
    description="python3 subscene api wrapper",
    keywords ="pypi packages subscene api wrapper subtitle downloader package python3",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/s-4-m-a-n/subscene-API",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages = ["subsceneAPI"],
    include_package_data = True, 
    install_requires=[
                    'beautifulsoup4==4.9.0',
                    'requests==2.23.0'
                        ],
    entry_points = {
        'console_scripts':['subsceneAPI=subsceneAPI.cli:main']
    }
)