
################## Scrape

import requests 
import requests 
from bs4 import BeautifulSoup 
  
URL = "https://quizlet.com/297264856/print"
r = requests.get(URL)  
soup = BeautifulSoup(r.content, 'html5lib') 


words = []
for word in soup.findAll('span', attrs = {'class' : 'left copy'}):
    words.append(word.text)

meanings = []
for meaning in soup.findAll('span', attrs = {'class' : 'right copy'}):
    meanings.append(meaning.text)


################### Store

import pandas as pd

df = pd.DataFrame({'Words' : words, 'Meanings' : meanings}, columns = ['Words', 'Meanings'])
df.to_csv('offenders.csv')