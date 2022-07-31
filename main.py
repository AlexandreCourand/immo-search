import requests
from bs4 import BeautifulSoup
import latlong
import cartimetown
import datetime

for page in range(89, 85, -1):
    url = 'https://www.bien-dans-ma-ville.fr/classement-ville-densite-normandie/?page=' + str(page)
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    for town in soup.find('tbody').find_all('tr'):
        town_name = town.a.string
        town_length = len(town_name)
        #print(town_name[0:town_length-5])
        #print(str(latlong.latlong(town_name[0:town_length-5])))
        #print(cartimetown.getTime(latlong.latlong(town_name[0:town_length-5])["long"], latlong.latlong(town_name[0:town_length-5])["lat"]))
        timeBeetweenTown = cartimetown.getTime(latlong.latlong(town_name[0:town_length-5])["long"], latlong.latlong(town_name[0:town_length-5])["lat"])
        if int(timeBeetweenTown.seconds/3600) < 3:
            print(town_name)
            #print(timeBeetweenTown)
        #print(int(cartimetown.getTime(latlong.latlong(town_name[0:town_length-5])["long"], latlong.latlong(town_name[0:town_length-5])["lat"]).seconds/3600))