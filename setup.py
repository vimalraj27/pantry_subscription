from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pantry/__init__.py
from pantry import __version__ as version

setup(
	name="pantry",
	version=version,
	description="Pantry Subscription System",
	author="Vimalraj R",
	author_email="vimalraj2772000@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
