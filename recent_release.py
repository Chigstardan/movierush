import time
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen


req = Request("https://www.thenetnaija.com/videos/movies", headers={'User-Agent': 'XYZ/3.0'})
req2 = Request("https://www.thenetnaija.com/videos/series", headers={'User-Agent': 'XYZ/3.0'})
webpage = urlopen(req, timeout=10)
webpage2 = urlopen(req2, timeout=10)
b4 = BeautifulSoup(webpage, "html.parser")
b5 = BeautifulSoup(webpage2, "html.parser")	
movie_list = b4.find_all("div", {"class" : "video-files"})
series_list = b5.find_all("div", {"class" : "video-files"})
printed = set()
while True:
	for movies in movie_list:
		movie_name = movies.find('img').get('alt')
		if movie_name not in printed:
			printed.add(movie_name)
			print(movie_name)
			requests.get("https://api.telegram.org/bot2008959598:AAEapVykIXdphGYaH5ZjXuhpFaFw7wpi5Bs/sendMessage?chat_id=805427106&text={}".format(movie_name))

	for series in series_list:
		series_name = series.find('img').get('alt')
		if series_name not in printed:
			printed.add(series_name)
			print(series_name)
			requests.get("https://api.telegram.org/bot2008959598:AAEapVykIXdphGYaH5ZjXuhpFaFw7wpi5Bs/sendMessage?chat_id=805427106&text={}".format(series_name))

	time.sleep(1800)