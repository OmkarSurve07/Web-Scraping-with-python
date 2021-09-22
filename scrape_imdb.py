'''
Installation:
1. install bs4 (pip install bs4)
2. install requests(pip install requests)
3. install pandas(pip install pandas)

'''

from bs4 import BeautifulSoup
import requests
import pandas as pd

# Get rae HTML data
url = "https://www.imdb.com/chart/top"

res = requests.get(url=url)

# Parse data by BeautifulSoup

soup = BeautifulSoup(res.text, features="html.parser")

all_tr = soup.findChildren("tr")

# Create data structure
title_list = []
year_list = []
rating_list = []

movie_data = {}

# Get data from TR table row and TH table data
for movie in all_tr:
    try:
        title_list.append(movie.find("td",{"class":"titleColumn"}).find("a").contents[0])
        year_list.append(movie.find("td",{"class":"titleColumn"}).find("span",{"class":"secondaryInfo"}).contents[0])
        rating_list.append(movie.find("td",{"class":"ratingColumn imdbRating"}).find("strong").contents[0])
    except:
        continue

# Organizing the data to data structures list and dict
movie_data["title"] = title_list
movie_data["year"] = year_list
movie_data["rating"] = rating_list

# Use pandas to create dataframe
df = pd.DataFrame(movie_data)
# print(df.head())

# store data in csv or excel file
print("csv file is on the way...")
df.to_csv("top_movies.csv")

# print("excel file is on the way...")
# df.to_excel("top_movies.xlsx")



