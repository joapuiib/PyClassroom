from setuptools import setup

setup(
    name='PyClassroom',
    version='0.0.1',
    author='Joan Puigcerver',
    author_email='joapuiib@gmail.com',
    maintainer='Joan Puigcerver',
    maintainer_email='joapuiib@gmail.com',
    packages=['pyclassroom'],
    url='',
    license='LICENSE',
    description='Google Classroom API made easy.',
    long_description=open('README.rst').read(),
    install_requires=[
        "pydrive >= 1.3.2",
    ],
)
