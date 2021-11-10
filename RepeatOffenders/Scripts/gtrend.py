from pytrends.request import TrendReq
import pandas as pd

df = pd.read_csv('offenders.csv')
words = list(df['Words'])

pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload([words[0]], cat=0, timeframe='today 12-m', geo='', gprop='')
dfTemp = pytrends.interest_over_time()
dfTrend = dfTemp[words[0]]

i = 0
for word in words:
    if word == words[0]:
        pass
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([word], cat=0, timeframe='today 12-m', geo='', gprop='')

    dfTemp = pytrends.interest_over_time()
    #dfTemp = dfTemp[word]
    dfTrend = pd.concat([dfTrend, dfTemp], axis = 1)

    i += 1
    if(i % 5 == 0):
        print((i / 699) * 100, '%')


print(dfTrend.info())

dfTrend.to_csv('data/trend.csv')