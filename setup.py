from setuptools import find_packages, setup
from typing import List

hypen_E_dot = '-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    This function will return the list of requirments 
    '''
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace('\n','') for req in requirments]

        if hypen_E_dot in requirments:
            requirments.remove(hypen_E_dot)
    return requirments


setup(
    name='MLProject',
    version='0.0.1',
    author='Sai Madisetty',
    author_email='madisettyjagadeesh@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
)