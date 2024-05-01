from setuptools import find_packages, setup
#from typing import List

def get_requirements()->list[str]:
    
    requirements_list=list[list]=[]
    
    return requirements_list

setup(
    
    name='sensor',
    version="0.0.1",
    author='Abdul',
    author_email='abdul44haseeb@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()  #["pymongo"]
)
    
    