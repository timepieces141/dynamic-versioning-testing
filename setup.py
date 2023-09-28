'''
Build and distribute the example tool.
'''


# core libraries
import pathlib


# third parties libraries
from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel


class DynamicVersionBDistWheel(bdist_wheel):
    pass


# packages
PACKAGE_DIR = {"": "src"}

# scripts
SCRIPTS = []

# the directory of this setup file
SETUP_DIR = pathlib.Path(__file__).parent

# README
README = (SETUP_DIR / "README.md").read_text()

# source directory
SRC_DIR = SETUP_DIR / "src"


def get_install_requires():
    '''
    Read the requirements file in as a list of project/version requirement
    specifications.
    '''
    with open((SETUP_DIR / "requirements.txt")) as install_fp:
        install_requires = install_fp.read().split("\n")
    return [req for req in install_requires if req]


def get_extras_require():
    '''
    Retrieves the various "extra" dependencies.
    '''
    extras = {}
    for extra in ["dev", "dist", "docs"]:
        req_file = SETUP_DIR / f"{extra}-requirements.txt"
        if req_file.exists():
            with open(req_file) as extra_fp:
                requires = extra_fp.read().split("\n")
                extras[extra] = [req for req in requires if req]

    return extras


setup(
    name="dynamic-versioning-testing",
    version=None,
    description="Example python distro package for testing dynamic versioning",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Edward Petersen",
    author_email="edward.petersen@gmail.com",
    package_dir=PACKAGE_DIR,
    packages=find_packages(SRC_DIR),
    scripts=SCRIPTS,
    install_requires=get_install_requires(),
    extras_require=get_extras_require(),
    cmdclass={"bdist_wheel": DynamicVersionBDistWheel}
)