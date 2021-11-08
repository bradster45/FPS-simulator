from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="fps_sim",
    version="0.0.1",
    author="Brad Fordham",
    author_email="bradleyfordham@hotmail.co.uk",
    description="A simple fps_sim",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/bradster45/fps_sim/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)