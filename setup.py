
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="GodingWal-game-utils",
    version="1.2",
    author="Goding Wal",
    author_email="datacreativellc@gmail.com",
    description="Gameplay logic for Rock-Paper-Scissors",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/GodingWal/game-utils-py",
    keywords="rock paper scissors game",
    packages=find_packages() # ["game_utils"]
)
