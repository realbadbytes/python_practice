from setuptools import find_packages
from cx_Freeze import setup, Executable

setup(
        name='Example Package',
        version='0.1',
        description='Tits Mcgee',
        author='no one',
        packages=find_packages(exclude=['docs', 'test']),
        install_requires=['requests'],
        executables = [Executable("sample.py")],
        package_data={
            'sample' : ['package_data.dat']
            },
        entry_points={
            'console_scripts' : [
                'hello=example_package.cli:say_hello',
                ]
            },
        license='MIT',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 3.5',
            ]
        )
