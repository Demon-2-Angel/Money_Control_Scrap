from setuptools import setup, find_packages

setup(
    name='Money_Control_Scrap',
    version='0.1.0',
    author="Aniruddha Kumar",
    author_email="foraniruddhakumar@gmail.com",
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
