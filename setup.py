from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    pass

setup(
    name = "end-to-end-ml-project",
    author= "sreeman",
    author_email= "sreemanbitsmech@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements("requirements.txt")
)

