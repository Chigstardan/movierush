import time
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

pages = ["movies", "series"]
printed = []
for page in pages:
    req = Request("https://www.thenetnaija.com/videos/" + page, headers={'User-Agent': 'XYZ/3.0'})

    webpage = urlopen(req, timeout=10)

    b4 = BeautifulSoup(webpage, "html.parser")

    movie_list = b4.find_all("div", {"class" : "video-files"})


    for OldContainers in movie_list:
	filmName = OldContainers.find('img').get('alt')
	printed.append(filmName)
	print(printed)
    for old in printed:
	requests.get("https://api.telegram.org/bot2008959598:AAEapVykIXdphGYaH5ZjXuhpFaFw7wpi5Bs/sendMessage?chat_id=805427106&text={}".format(old))

new_release = []

while True:
    for page in pages:
	req = Request("https://www.thenetnaija.com/videos/" + page, headers={'User-Agent': 'XYZ/3.0'})
	webpage = urlopen(req, timeout=10)
	b4 = BeautifulSoup(webpage, "html.parser")
	movie_list = b4.find_all("div", {"class" : "video-files"})
		
	for NewContainers in movie_list:
	    new_filmName = NewContainers.find('img').get('alt')
	    new_release.append(new_filmName)
	if new_release != printed:
	    for get in new_release:
		requests.get("https://api.telegram.org/bot2008959598:AAEapVykIXdphGYaH5ZjXuhpFaFw7wpi5Bs/sendMessage?chat_id=805427106&text={}".format(get))
	time.sleep(1800)
