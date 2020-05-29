'''
Shawn Dolifka
29 Sep 2019
'''

import requests
import csv
from bs4 import BeautifulSoup

#Get the webpage information
data = requests.get("https://www.census.gov/programs-surveys/popest.html").text
page_soup = BeautifulSoup(data, features='lxml')

urls = []

for link in page_soup.find_all('a'):
    #Check if the link is set to None or if it just leads to a different section on same page
    if str(link.get('href')) != 'None' and str(link.get('href')).startswith('#') == False:
        urls.append(link.get('href'))

#Relative paths start with '/', so loop though and add the absolute path to their beginning
i = 0
while i < len(urls):
    if urls[i].startswith('/'):
        urls[i] = 'https://www.census.gov' + urls[i]
    i += 1

#Convert the list to a set to remove duplicate items
urls = set(urls)

#Convert the set back to a list
urls_list = list(urls)

with open('URLs.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(urls_list)
        
#Lines used to get screenshots for Assessment. Uncomment to see screencapped results
'''
urls_list.sort()
print(*urls_list, sep = "\n")
print(len(urls_list))
'''