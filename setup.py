# This setup file is based on the one found here:
# https://towardsdatascience.com/create-your-custom-python-package-that-you-can-pip-install-from-your-git-repository-f90465867893

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='emv',
    version='0.4.1',
    author='I.N.Tzortzis',
    author_email='i.n.tzortzis@gmail.com',
    description='EMV_tool installation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/itzortzis/EMV_tool',
    project_urls = {
        "Code": "https://github.com/itzortzis/EMV_tool",
        "Bug Tracker": "https://github.com/itzortzis/EMV_tool/issues"
    },
    license='GPL-3.0',
    packages=['emv'],
    install_requires=['numpy', 'scipy', 'matplotlib'],
)
