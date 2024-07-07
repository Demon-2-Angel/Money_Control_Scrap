from setuptools import setup, find_packages

# Read the content of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='Money_Control_Scrap',
    version='0.1.2',
    author="Aniruddha Kumar",
    author_email="foraniruddhakumar@gmail.com",
    description="A package to scrape news from Money Control",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'Money_Control_Scrap=src.main:fetch_news_headlines',
        ],
    },
)
