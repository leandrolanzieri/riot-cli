
from setuptools import setup, find_packages
from riotcli.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='riotcli',
    version=VERSION,
    description='CLI tool for RIOT OS',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='RAPstore',
    author_email='rapstore@riot-apps.net',
    url='https://github.com/johndoe/myapp/',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'riotcli': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        riotcli = riotcli.main:main
    """,
)
