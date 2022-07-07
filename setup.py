from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf8")

setup(
    name='openbk',
    packages=find_packages(),
    version='1.0.0',
    description='A python library to easily extract information and metrics from Moroccan bank statements.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Imad Archid',
    author_email='hello@imadarchid.com',
    license='GPL',
    url='https://github.com/imadarchid/openbk',
    install_requires=['tabula-py', 'pandas', 'PyPDF2'],
    python_requires='>=3.10',
)
