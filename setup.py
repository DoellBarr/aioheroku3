from setuptools import setup

setup(
    name='herokupy',
    version='1.0',
    packages=['herokupy', 'herokupy.errors', 'herokupy.methods', 'herokupy.methods.accounts'],
    url='https://github.com/DoellBarr/herokupy',
    license='MIT',
    author='ShohihAbdul',
    author_email='shohih242@gmail.com',
    description='Asynchronous Heroku wrapper library.'
)
