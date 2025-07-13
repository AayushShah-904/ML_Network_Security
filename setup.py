'''
The setup.py file is an essential part of packaging and distributing Python projects.It is used by setuptools
(or distutils in older Python versions) to define the configuration of your project, such as metadata, dependencies and more
'''

from setuptools import find_packages,setup

from typing import List

requirements_list:List[str]=[]
def get_requirements()->List[str]:
    '''return list of requirements'''
    try:
        with open('requirements.txt','r') as f:
            lines=f.readlines()
            #precess each line
            for line in lines:
                requirements=line.strip()
                #ignore emtpy line and -e .
                if requirements and requirements!='-e .':
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print("Requirements.txt file not found ")

    return requirements_list

setup(
    name='Network-Security',
    version='0.0.1',
    author='Aayush Shah',
    author_email='aayushshah904@gmail.com',
    description='Network Security Project',
    packages=find_packages(),
    install_requries=get_requirements()
)