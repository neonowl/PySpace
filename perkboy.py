# Fallout 76 Perk Viewer
# Work in progress...

import bs4
import requests

# Get perks page 
def souper(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    return soup

# Parse SPECIAL stat names
def get_stat_names(soup_object):
    stats = []
    stat_names = soup_object.find_all("span", class_="mw-headline")
    del stat_names[0:2]
    for name in stat_names:
        stats.append(name.text)
    return stats

# Parse the perk names
def get_perk_names(soup_object):
    perks = []
    perk_table = soup_object("table")[5:12]
    for table in perk_table:
        perk_names = table.find_all("a")
        for name in perk_names:
            perks.append(name.text)
    return perks

def perks_by_stat(soup_object):
    stat_names = soup_object.find_all("span", class_="mw-headline")
    del stat_names[0:2]
    perk_table = soup_object("table")[5:12]
    perk_dict = {}
    for stat,table in zip(stat_names,perk_table):
        perk_dict[stat.text] = {}
        perk_names = table.find_all("a")
        for name in perk_names:
            perk_dict[stat.text][name.text] = {}
    return perk_dict

soup = souper('https://fallout.gamepedia.com/Fallout_76_perks')

all_perks = perks_by_stat(soup)

print(str(all_perks))

# TO-DO
# 
# Output individual perk descriptions & ranks
