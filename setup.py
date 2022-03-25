from setuptools import setup, find_packages

setup(
    name='pydsa',
    packages=find_packages(include=['pydsa']),
    version='0.1.0',
    description='Python Data Structures Library',
    author='astrica1',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)