from typing import List
from setuptools import setup, find_packages

HYPEN_E_DOT = '-e.'


def read_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="",
    version="0.0.1",
    author="Dhruval Bhuva",
    author_email="dhruvalbhuva2000@gmail.com",
    packages=find_packages(),
    install_requires=read_requirements("requirements.txt"),
)
