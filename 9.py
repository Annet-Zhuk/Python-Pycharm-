from urllib.request import urlopen, urlretrieve
from collections import defaultdict
from bs4 import BeautifulSoup
html = open('test.txt', 'r', encoding="utf-8").read()
soup = BeautifulSoup(html)
s =[]
for link in soup.find_all('code'):
    s.append(link)

dic = defaultdict(int)
for num in s:
    dic[num] += 1

s_list = sorted(dic, key=dic.__getitem__, reverse=True)

new_list = []
for num in s_list:
    for rep in range(dic[num]):
        new_list.append(num)

print(new_list)
