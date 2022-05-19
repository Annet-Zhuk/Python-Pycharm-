from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request as urlrq
import certifi
import ssl
lxml = open('test.txt', 'r', encoding="utf-8").read()
soup = BeautifulSoup(lxml, 'lxml')
nodes = {}
for node in soup.find_all('node'):
    lat =float(node['lat'])
    lon = float(node['lon'])
    id = int(node['id'])
    nodes[id] = (lat, lon)
for way in soup.find_all('way'):
    flag = False
    for tag in way ('tag'):
        if tag['k'] == 'building':
            flag = True
    if flag:
        rnodes = []
        for nd in way('nd'):
            ref = int(nd['ref'])
            rnodes.append(ref)
        s = (len(rnodes))
        r0 = (rnodes[0])
        rmax = rnodes[s-1]
        if r0 == rmax:
            id = way['id']
            print(id)
            f = []
            for k in range (s):
                coor1 = nodes[rnodes[k]]
                f.append(coor1)
            print(f)

