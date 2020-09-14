import requests
import bs4
def scrap_img(name):
    """This function receive a name parameter in order to do web scrapping to extraxt images of Harry Potter Character"""

    res=requests.get('https://harrypotter.fandom.com/es/wiki/'+name)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    res=requests.get('https://harrypotter.fandom.com/es/wiki/'+name)
    soup=bs4.BeautifulSoup(res.text,'lxml') 
    if name == 'Dudley Dursley':
        img=soup.select('figure')[0].select('img')[1].get('src')
        return img
    else:    
        try:
            img=soup.select('aside')[0].select('img')[0].get('src')
            return img
        except:
            return 'No picture available'

