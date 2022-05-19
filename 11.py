from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request as urlrq
import certifi
import ssl
import math


def getsqr(coordlist):
    baselat = coordlist[0][0]
    baselon = coordlist[0][1]
    degreelen = 111300
    newcoord = []
    for now in coordlist:
        newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.sin(baselat)))
    sqr = 0
    for i in range(len(newcoord) - 1):
        sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
    sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
    return abs(sqr)

lxml = open('test.txt', 'r', encoding="utf-8").read()
soup = BeautifulSoup(lxml, 'lxml')
nodes = {}
sdommax = 0
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

            coordlist = []
            for k in range (s):
                coor1 = nodes[rnodes[k]]
                coordlist.append(coor1)
            sdom = (getsqr(coordlist))
            if sdom > sdommax:
                sdommax = sdom
                print(id, sdommax)
