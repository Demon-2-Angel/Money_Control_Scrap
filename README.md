# Product Delivered By Aniruddha Kumar

# Money_Control_Scrap

Money_Control_Scrap is a Python package for scraping the latest business news from the Money Control website (One of the biggest website on Finance ion India)

## Features

- Scrape news headlines, links, and publication times from Money Control.
- Save the scraped data to a CSV file.
- The CSV contains, date-time, Headline and the Link to that site

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Money_Control_Scrap.

```bash
pip install Money_Control_Scrap
```



## Usage
### Importing and Using the Package

python
```
from Money_Control_Scrap import fetch_news_headlines

# Define the full path to the chromedriver
chromedriver_path = r"./path_to_chrome_driver" 

# Fetch the news headlines
csv_path = fetch_news_headlines(chromedriver_path)
print(f"News headlines saved to: {csv_path}")

# Fetch news headlines and save to CSV
fetch_news_headlines()
```

### Command Line Interface
After installing the package, you can also run the scraper directly from the command line:

```
Money_Control_Scrap /path_to_chrome_driver
```
## Development
### Project Structure

```
Money_Control_Scrap/
    __init__.py
    main.py
.github/
    workflows/
        python-package.yml
setup.py
requirements.txt
README.md

```
### Setup for Development

1. Clone the repository:

```
git clone https://github.com/your-username/Money_Control_Scrap.git
cd Money_Control_Scrap
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change

## Contact
For any inquiries, please contact Aniruddha Kumar at foraniruddhakumar@gmail.com.
