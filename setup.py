from setuptools import setup, find_packages

setup(
    name='load_balancer',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'flask',  # Add any other dependencies here
    ],
)
