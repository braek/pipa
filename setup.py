from setuptools import setup, find_packages

setup(
    name='pippa',
    version='0.1',
    description='Pippa Data Pipeline',
    long_description='',
    author='Koder BV',
    author_email="kristof@koder.be",
    license='MIT',
    url='https://www.koder.be',
    include_package_data=True,
    package_data={},
    packages=find_packages(),
    # install_requires=dependencies,
    # extras_require={
    #     'dev': test_dependencies
    # },
    scripts=['pippa/cli/pippa'],
    zip_safe=False
)
