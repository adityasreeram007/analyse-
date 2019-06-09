import urllib
import os
from bs4 import BeautifulSoup
import requests
container=[]
path=os.getcwd()
for filename in os.listdir(path):
    if filename.endswith(".html"):
        response = urllib.request.urlopen('file:///C:/Users/Aditya%20Sreeram/Downloads/Telegram%20Desktop/ChatExport_09_06_2019/' + filename)
        print(filename)
        doc=response.read()
        #URL = "file:///C:/Users/Aditya%20Sreeram/Downloads/Telegram%20Desktop/ChatExport_09_06_2019/" + filename
        #print(URL)
        #r = requests.get(URL)
        #print(filename)
        soup=BeautifulSoup(doc,'html.parser')
        print(soup.prettify())
        container.append(soup)
print(container)
