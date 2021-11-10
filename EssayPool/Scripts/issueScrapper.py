import requests 
import pickle
from bs4 import BeautifulSoup

def scrapper():
    URL = "https://www.ets.org/gre/revised_general/prepare/analytical_writing/issue/pool"
    r = requests.get(URL)  
    soup = BeautifulSoup(r.content, 'html5lib')

    issue = []
    temp = ''

    for idx, i in enumerate(soup.findAll('div', attrs = {'class' : 'contents left'})[0].findAll('p')):
        if idx == 0:
            pass
        elif not('Write a response in which you' in i.text):
            temp += i.text + '\n'
        elif 'Write a response in which you' in i.text:
            if len(temp) != 0:
                issue.append(temp)
            temp = ''
            
    try:
        with open('data/issue.pkl', 'wb') as f:
            pickle.dump(issue, f)
    except:
        pass

    try:
        with open('issue.pkl', 'wb') as f:
            pickle.dump(issue, f)
    except:
        pass

    return 'done'

