from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data={}
    #Facts table with pandas
    path = "https://space-facts.com/mars/"
    table = pd.read_html(path)
    df = table[0]  
    fact = df.rename(columns={0:"Description",1:"Value"})
    fact_table= fact.set_index("Description")
    fact_table.to_html()
    mars_data["fact_table"] = fact_table
    
    browser.quit()
    return mars_data