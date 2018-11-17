from setuptools import setup, find_packages

setup(
        name='Example Package',
        version='0.1',
        description='Tits Mcgee',
        author='no one',
        packages=find_packages(exclude=['docs', 'test']),
        install_requires=['requests'],
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
