# Import libraries
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

#Ethical Header
#headers = {'User-Agent' : 'Data Science Student | Ryan Marshall marshallpryan@gmail.com'}

# Sets the starting url
url = 'http://www.millenniumrunning.com/2019-results'
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "lxml")

#Setup a list of all the races that were found on the results page
race_list_links = []

#Finds all races listed on the page and adds each link into a list based on html tags
for races in soup.find_all('h4',class_='rt-article-title'):
    for a in races.find_all('a'):
        print(a.get('href'))
        race_list_links.append(a.get('href'))
        time.sleep(2) 

'''
#########
#
# Navigate to each race url and find the printable results link
#
########
race_length = len(race_list_links)

for race in range(race_length):
    current_url = race_list_links[race]
    print(current_url)
    new_response = requests.get(current_url)
    new_soup = BeautifulSoup(new_response.text, "lxml")

    race_result_links = []

    for link in new_soup.find_all('a'):
        current_link = link.get('href')
        if current_link is not None:
            if ".html" in current_link:
                race_result_links.append(link.get('href'))
                print(link.get('href'))
        time.sleep(2)

#########
#
# Navigates to the printable results link and extracts the table
#
########
'''
