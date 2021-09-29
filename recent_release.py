import time
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

req = Request("https://www.thenetnaija.com/videos/movies", headers={'User-Agent': 'XYZ/3.0'})
webpage = urlopen(req, timeout=10)
b4 = BeautifulSoup(webpage, "html.parser")
movie_list = b4.find_all("div", {"class" : "video-files"})

for allContainers in movie_list:
    filmName = allContainers.find('img').get('alt')
printed = []
print(filmName)
while True:
	requests.get("https://api.telegram.org/bot2008959598:AAEapVykIXdphGYaH5ZjXuhpFaFw7wpi5Bs/sendMessage?chat_id=805427106&text={}".format(filmName))
	time.sleep(10)
	
