from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads a requirements file and returns a list of requirements.
    It removes any instances of '-e .' from the list.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='telco_churn_predictor',  # Update project name
    version='0.1.0',               # Use a more conventional version
    author='Omkar',
    author_email='om.data07@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
