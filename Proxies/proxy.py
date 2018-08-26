import requests
import os
from bs4 import BeautifulSoup


url = 'https://free-proxy-list.net/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

ip = {}
port = {}

table = soup.find_all('table')[0]
#Grabs IP
for row in table.find_all('tr')[1:]:
	try:
		ip[row] = ((row.td.get_text().encode()))
	except(TypeError, KeyError, AttributeError) as e:
		pass

#Grabs Ports
for row2 in table.find_all('tr')[1:]:
	try:
		port[row2] = ((row2.find_all('td')[1].text.encode()))
	except(TypeError, KeyError, AttributeError, IndexError) as e:
		pass

f = open("proxies.txt", "w+")

for i in ip:
	f.write(ip[i] + ":" + port[i] + "\n")
f.close()

print("Proxies saved in current script folder")