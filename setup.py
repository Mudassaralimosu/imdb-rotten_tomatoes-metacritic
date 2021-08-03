from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="imdb_rtomatoes_metacritic",
    version='0.0.1',
    description="A Single package which will help to get the imdb,rotten tomatoes and metacritic ratings,with this python package we can get the number of people/critic who reviewd it",
    py_modules=["imdb-rotten_tomatoes-metacritic"],
    package_dir={'': 'src'},

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.8.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],

    long_description=long_description,
    long_description_content_type="text/markdown",

    extra_requires = {
        "dev": [
            "pytest>=3.7",
            "beautifulsoup4"
        ],
    },

    url="https://github.com/Mudassaralimosu/imdb-rotten_tomatoes-metacritic",
    author="Mudassar Ali Ansari",
    author_email="mudassar786mosu@gmail.com"
)