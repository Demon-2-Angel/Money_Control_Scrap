from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

def fetch_news_headlines(chromedriver_path, website_url="https://www.moneycontrol.com/news/business/", headless=True):
    # Get the current directory of the executable
    application_path = os.path.dirname(sys.executable)
    
    # Get the current date for the filename
    now = datetime.now()
    month_day_year = now.strftime("%m%d%Y")
    
    # Set Chrome options
    options = Options()
    options.headless = headless

    # Create a Chrome service
    service = Service(executable_path=chromedriver_path)
    
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(website_url)
    
    # Lists to store the data
    time_of_news = []
    links = []
    headline_list = []
    
    # Get news elements
    news = driver.find_elements(By.XPATH, value="//div[@class='fleft']/ul/li[@class='clearfix']")
    
    for details in news:
        time = details.find_element(By.XPATH, value=".//span").text
        link = details.find_element(By.XPATH, value=".//a").get_attribute("href")
        headline = details.find_element(By.XPATH, value=".//a").get_attribute("title")
        time_of_news.append(time)
        links.append(link)
        headline_list.append(headline)
    
    # Create a DataFrame and save to CSV
    news_data = {'Time': time_of_news, 'Headline': headline_list, 'Link': links}
    df_news_data = pd.DataFrame(news_data)
    
    filename = f'news_headlines{month_day_year}.csv'
    final_path = os.path.join(application_path, filename)
    df_news_data.to_csv(final_path)
    
    # Quit the driver
    driver.quit()
    
    return final_path
