import requests, sys
from bs4 import BeautifulSoup
data = requests.get("https://timesofindia.indiatimes.com/rss.cms")
soup = BeautifulSoup(data.text, 'html.parser')

# link = soup.a
# print(link.get('href'))

# print(soup.a['class'])
# sys.exit()

for link in soup.find_all('a'):
    # print(link.get('class')) "rssurl"
    if link.get('class') == ['rssurl'] :
        currlink = link.get('href')
        # print(currlink)
        # break
        data1 = requests.get(currlink)
        # print(data1.text)
        # break
        soup1 = BeautifulSoup(data1.text, "lxml-xml")
        # print(soup1.prettify())
        # break
        if soup1.item != None:
            print(soup1.item.title.string)

