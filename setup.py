from setuptools import find_packages, setup

setup(
    name='openbk',
    packages=find_packages(),
    version='0.0.1',
    description='A python library to easily extract information and metrics from Moroccan bank statements.',
    author='Imad Archid',
    license='MIT',
    install_requires=['tabula-py', 'pandas'],
)
