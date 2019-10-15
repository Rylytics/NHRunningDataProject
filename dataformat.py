# Import libraries
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://www.millenniumrunning.com/wp-content/uploads/2014/09/OverallResults_KellyMannMemorial5k_2019.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "lxml")

#Extract rows and clean the values
rows = soup.find_all('tr')
list_rows = []

for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)

type(clean2)

#create the dataframe
df = pd.DataFrame(list_rows)

#Create the dataframe columns
df1 = df[0].str.split(',', expand=True)

#Strip out the brackets
df1[0] = df1[0].str.strip('[')

#Find the headers for the columns
col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)

#Convert the headers into a dataframe
df2 = pd.DataFrame(all_header)
df3 = df2[0].str.split(',', expand=True)

#Setup and combine the frames
frames = [df3, df1]
df4 = pd.concat(frames)

#Assign rows
df5 = df4.rename(columns=df4.iloc[0])

#Drop rows missing values
df6 = df5.dropna(axis=0, how='any')

#Drop duplicated header
df7 = df6.drop(df6.index[0])
df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Deltadiv]': 'Deltadiv'},inplace=True)
df7['Deltadiv'] = df7['Deltadiv'].str.strip(']')

print(df7.head())
#df7.to_csv('export.csv')