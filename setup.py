
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='EMV_tool',
    version='0.1.0',
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
    packages=['EMV_tool'],
    install_requires=['numpy', 'scipy', 'matplotlib'],
)
