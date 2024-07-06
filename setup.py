from setuptools import setup, find_packages


setup(
    name='Money_Control_Scrap',
    version='0.1.0',
    author="Aniruddha Kumar",
    author_email="foraniruddhakumar@gmail.com",
<<<<<<< HEAD
    description="A package to install and scrap the money control website into an Excel file to get the links and the headlines of the Financial News",
=======
    description="A package to install and scrap the money control website into an Excel file to get the links and the headlines of the Financial News"
>>>>>>> 24767de497289813a0bf94c2c50bb71a4d2f29ee
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