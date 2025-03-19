from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''Returns a list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]


    return requirements



setup(
name='ML_Project',
version='0.0.1',
author='Sangam',
author_email='sangamsrivastav2002@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)