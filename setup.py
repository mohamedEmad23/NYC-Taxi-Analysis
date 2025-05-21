from setuptools import setup, find_packages

setup(
    name='nyc-taxi-analysis',
    version='0.1',
    author='Mohammed Emad',
    author_email='mohammed.emad4884@gmail.com',
    description='A project for analyzing NYC taxi trip data using Cassandra and Spark.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'pyspark',
        'cassandra-driver',
        'matplotlib',
        'seaborn',
        'jupyter'
    ],
    entry_points={
        'console_scripts': [
            'nyc-taxi-analysis=main:main',
        ],
    },
)