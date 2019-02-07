# Fallout 76 Perk Scraping Script
# Work in progress...

import bs4
import requests

def souper(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    return soup

def get_stat_names(soup_object):
    stats = []
    
    stat_names = soup_object.find_all("span", class_="mw-headline")
    del stat_names[0:2]

    for name in stat_names:
        stats.append(name.text)

    return stats


soup = souper('https://fallout.gamepedia.com/Fallout_76_perks')

SPECIAL = get_stat_names(soup)

for name in SPECIAL:
    print(name)
