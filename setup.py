from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(


name='pypdf2text',

version = '1.0.0',


description='A program to convert pdf files to text files.',


author_email='kk1478@msstate.edu',


keywords='pdf, text',


py_modules=['run'],


python_requires='>=3',



install_requires=['pytesseract','opencv-python','pdf2image']


)



