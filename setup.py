from setuptools import find_packages,setup
from typing import List

Hypen_E_dot = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirents = [req.replace("\n","") for req in requirements]

        if Hypen_E_dot in requirements:
            requirements.remove(Hypen_E_dot)
    return requirements


setup(
name = 'mlproject',
version ='0.0.1',
author = 'Darshan',
author_email = 'darshan.patil1104@gmail.com',
packages = find_packages(),
install_requires =get_requirements('requirements.txt'),
)

