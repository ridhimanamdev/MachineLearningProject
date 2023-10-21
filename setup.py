from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOR='-e.'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of the requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOR in requirements:
            requirements.remove(HYPEN_E_DOR)
    
    return requirements


setup(
    name='MachineLearningProject',
    version='0.0.1',
    author='Ridhima',
    author_email='ridhimanamdev84145@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)