from setuptools import find_packages, setup

setup(
    name='Mise_en_prod_projet',
    version='0.1',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
