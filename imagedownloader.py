from genericpath import exists
import requests
from bs4 import BeautifulSoup

url = 'https://oldschool.runescape.wiki/w/Quests/List'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
urlList = []
for link in soup.find_all("a"):
    if link.has_attr('href'):
        urlList.append('https://oldschool.runescape.wiki' + link.attrs['href'])
    else:
        pass


for url in urlList:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img', width=488, height=320)
    for image in images:
        name = image['alt']
        link = 'https://oldschool.runescape.wiki/images/' + str(image['alt']).replace(' ','_')
        with open(name.replace(' ', '-').replace('/', '') + '.png', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)