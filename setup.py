from setuptools import find_packages, setup
from typing import List


# Function to install requirements from the requirements.txt file
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines() if not req.strip().startswith("#")]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
        

setup(
    name='machine_learning_project',
    version='1.0.0',
    author='Joshua Maeba',
    author_email='joshuamaeba@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
