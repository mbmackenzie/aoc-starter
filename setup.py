from setuptools import setup, find_packages

setup(
    name="advent-of-code",
    version="0.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click",],
    entry_points={"console_scripts": ["aoc = solutions.scripts.aoc:cli",],},
)
