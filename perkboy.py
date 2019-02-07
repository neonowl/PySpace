# Fallout 76 Perk Scraping Script
# Work in progress...

import bs4
import requests

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

soup = souper('https://fallout.gamepedia.com/Fallout_76_perks')

SPECIAL = get_stat_names(soup)

all_perks = get_perk_names(soup)

for perk in all_perks:
    print(perk)

# TO-DO
# 
# List perks by their SPECIAL stat
# Display perk info
# Write perks to a file
