import requests
newsurl = ('http://newsapi.org/v2/top-headlines?country=ie&apiKey=820ad7802a5046fc99f7e906f7817f1c')
response = requests.get(newsurl)
#print(response.json())

news = []
for i in response.json()['articles']:
    article = {}
    #print(str(i['source']['name']) + ": " + str(i['author']))
    article['source'] = str(i['source']['name']) + ": " + str(i['author'])
    #print(i['title'])
    article['title'] = i['title']
    #print(i['description'])
    article['description'] = i['description']
    #print(i['url'])
    article['url'] = i['url']
    #print('')
    news.append(article)
    
print(news)