from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data={}
    
    # News
    news_url="https://mars.nasa.gov/news/"
    browser.visit(news_url)    
    html=browser.html
    news_s=bs(html,"html.parser")
    #title
    news=news_s.find_all("div", class_="content_title")
    news_title = news[0].text.strip()
    mars_data["news_title"] = news_title
    #paragraph
    news_p = news_s.find_all("div", class_="rollover_description_inner")[0].text.strip()
    mars_data["news_p"] = news_p
    
    #Featured Image
    feature_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(feature_url)
    time.sleep(2)
    browser.find_by_css("a#full_image.button.fancybox").click()
    featured_image_url=browser.find_by_css("img.fancybox-image")["src"]
    mars_data["featured_image_url"] = featured_image_url
   

    #Weather@twitter
    path = "https://twitter.com/marswxreport?lang=en"
    weather = requests.get(path)
    weather_soup=bs(weather.text,"html.parser")
    weather_info = weather_soup.find_all("div",class_="js-tweet-text-container")
    mars_weather = weather_info[0].find("p").text
    mars_data["mars_weather"] = mars_weather
    
    
    
    #Facts table with pandas
    path = "https://space-facts.com/mars/"
    table = pd.read_html(path)
    df = table[0]
    df.columns = ["Description","Value"]
    df.set_index('Description', inplace=True)
    fact_table=df.to_html()
    mars_data["fact_table"] = fact_table
    

    
    
    #Mars Hemispheres
    h="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    r=requests.get(h)
    s=bs(r.text,"html.parser")
    titles=s.find_all("div", class_="description")
    t_list=[]
    for i in range(len(titles)):
        t_list.append(titles[i].find("h3").text)
     
   
    
    #h_LINK
    browser.visit(h)
    link_list=[]
    for x in range(len(browser.find_by_css("a.product-item h3"))):
        browser.find_by_css("a.product-item h3")[x].click()
        link_list.append(browser.find_by_css("img.wide-image")["src"])
        browser.back()
    link_list
    
    
    hemisphere_image_urls = [
    {"title": t_list[0], "img_url": link_list[0]},
    {"title": t_list[1], "img_url": link_list[1]},
    {"title": t_list[2], "img_url": link_list[2]},
    {"title": t_list[3], "img_url": link_list[3]},]
    
    mars_data["hemisphere_image_urls"] = hemisphere_image_urls
    
    browser.quit()
    return mars_data
        
        
    
    
    
    
    
    
    
    
    
    
    
   