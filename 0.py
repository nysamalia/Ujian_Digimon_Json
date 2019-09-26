from bs4 import BeautifulSoup
import requests
import json

req = requests.get('http://digidb.io/digimon-list/')
soup = BeautifulSoup(req.content, 'html.parser')

data = soup.find('tbody')
data = data.find_all('tr')

digimons= []
for i in data:
    no = i.find('td', width='5%').b.text
    digimon = i.a.text
    image = i.img['src']
    stage = i.center.text
    tipe = i.find('td', width='7%').text
    attribute = i.find('td', width='7%').find_next_sibling().text
    memory = i.find('td', width='7%').find_next_sibling().find_next_sibling().text
    equip = i.find('td', width='8%').text
    feature = i.find_all('td', width=False)
    
    feature_list = []
    for i in feature:
        feature_list.append(i.string)
    
    x = {
        'no': int(no),
        'digimon': digimon,
        'image': image,
        "stage": stage,
        'type': tipe,
        'attribute': attribute,
        'memory': int(memory),
        'equip slots': int(equip),
        "hp": int(feature_list[0]),
        "sp": int(feature_list[1]),
        "atk":int(feature_list[2]),
        "def":int(feature_list[3]),
        "int":int(feature_list[4]),
        "spd":int(feature_list[5])
    }
    digimons.append(x)

with open('digimon.json', 'w') as digi:
    json.dump(digimons, digi)