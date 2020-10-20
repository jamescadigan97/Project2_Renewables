#Import Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import pymongo
import requests
from splinter import Browser
from datetime import date
from flask_pymongo import PyMongo
import datetime
import json

renewables = { }
now = datetime.datetime.now()
print ("Current date and time : ")
last_refresh = now.strftime("%Y-%m-%d %H:%M:%S")
print(last_refresh)
renewables.update({"renewable_refresh": last_refresh })

def renewable_scrape():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://www.renewableenergyworld.com"
    #base_url = "https://www.renewableenergyworld.com"
    browser.visit(url)
    #response4 = requests.get(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    link_list = []
    title_list = []
    browser.visit(url)

    renewables = {}
    now = datetime.datetime.now()
    print ("Current date and time : ")
    last_refresh = now.strftime("%Y-%m-%d %H:%M:%S")

    ##This Line
    renewables.update({"renewable_refresh": last_refresh })

    for x in range (5):
        #url = "https://www.renewableenergyworld.com"
        link_ = soup.findAll('article')
        link = link_[x].find('link').get('href')
        link_list.append(link)
        link_ = soup.findAll('article')
        title = link_[x].find('h2', class_='post-list-item__title').find('a').text
        link_list.append(link)
        title_list.append(title)

        ##These two lines
    renewables.update({"renewable_links": link_list })
    renewables.update({"renewable_titles": title_list })
        
    now = datetime.datetime.now()
    print ("Current date and time : ")
    last_refresh = now.strftime("%Y-%m-%d %H:%M:%S")
        # renewables.update({"renewable_refresh": last_refresh })
    renewables = {"links": link_list, "articles ": title_list, "last_scrape": last_refresh}

    out_file = open("my_renewables.json", "w") 
  
    json.dump(renewables, out_file, indent = 6) 