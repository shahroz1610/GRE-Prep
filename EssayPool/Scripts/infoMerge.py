import pandas as pd
import numpy as np

dfWord = pd.read_csv('offenders.csv')
dfTrend = pd.read_csv('data/trend.csv')

words = list(dfWord['Words'])
meanings = list(dfWord['Meanings'])
trends = []

notWord = ['abstemioius', 'idolatrious', 'inerlocutor']

for word in words:
    if word in notWord:
        pass
    else:
        trends.append(np.round(dfTrend.loc[:, word].mean()))

for word in notWord:
    idx = words.index(word)
    words.pop(idx)
    meanings.pop(idx)

df = pd.DataFrame({'Words' : words, 'Meanings' : meanings, 'Trends' : trends}, columns = ['Words', 'Meanings', 'Trends'])
df.to_csv('test.csv')


