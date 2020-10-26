#Import Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import pymongo
import requests
from splinter import Browser
from datetime import date
from flask_pymongo import PyMongo
import datetime

renewables = { }

def renewable_scrape():
    #Launch chromedriver and visit page
    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://www.renewableenergyworld.com"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    link_list = []
    title_list = []
    browser.visit(url)

    #Get current date and time
    now = datetime.datetime.now()
    print ("Current date and time : ")
    last_refresh = now.strftime("%Y-%m-%d %H:%M:%S")

    #Upload to the MongoDB
    renewables.update({"renewable_refresh": last_refresh })

    #Loop through pages to get articles and links
    for x in range (5):
        link_ = soup.findAll('article')
        link = link_[x].find('link').get('href')
        link_list.append(link)
        link_ = soup.findAll('article')
        title = link_[x].find('h2', class_='post-list-item__title').find('a').text
        link_list.append(link)
        title_list.append(title)

    #Update Mongo DB
        renewables.update({"renewable_links": link_list })
        renewables.update({"renewable_titles": title_list })
        
    #Get current date and time
        now = datetime.datetime.now()
        print ("Current date and time : ")
        last_refresh = now.strftime("%Y-%m-%d %H:%M:%S")
        renewables.update({"renewable_refresh": last_refresh })
    browser.quit()
    return renewables