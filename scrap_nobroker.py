import requests
from bs4 import BeautifulSoup

url = "https://www.nobroker.in/prophub/new-builder-projects/new-builder-projects-in-bangalore/"

res = requests.get(url=url)
content_html = res.content

soup = BeautifulSoup(content_html,'html.parser')
# print(soup.prettify())
print(soup.title.text)

project_name = []
property_details = {"project_name":[],"price":[],"bhk":[]}

for inner_ul in soup.find_all('ul'):
    for inner_li in inner_ul:
        for inner_most_li in inner_li:
            if "Project Name" in inner_most_li:
                property_details["project_name"].append(inner_most_li.strip().split(":")[1])
            if "Price" in inner_most_li:
                property_details["price"].append(inner_most_li.strip().split(":")[1])
            if "BHK Type" in inner_most_li:
                property_details["bhk"].append(inner_most_li.strip().split(":")[1])

print(property_details)