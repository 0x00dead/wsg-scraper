#!/usr/bin/env python

import requests
import json
import sqlite3
import re

#get the catalog
def cat_message():
   print "Downloading the catalog....      ",
#download the catalog in chunks so it takes less time
response = requests.get('http://a.4cdn.org/wsg/catalog.json', stream=True)
with open('catalog.json', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
response.close()
cat_message()
print "[DONE]"

#pretty up the catalog
def pp_message():
   print "Prettying up the JSON....        ",
#read the catalog.json, save the pretty version into a var then write it to pretty.json
with open('catalog.json') as op:
	data = json.load(op)
pretty = json.dumps(data, indent=4, sort_keys=True)
with open('pretty.json', 'w') as outfile:  
    outfile.write(pretty)
pp_message()
print "[DONE]"

#scrape the threads
def db_message():
   print "Scraping the catalog....      ",
conn = sqlite3.connect('database.db')
c = conn.cursor()
#connect to the db then scrape the threads
with open('pretty.json') as f:
	data = json.load(f)
for pg in range(11):
	for th in range(15):
		try:
			current = data[pg]["threads"][th]
			#it's checking if it sees * in the comment or the name, if it does, then it inserts it into the db
			if (current["sub"].find('YLYL') != -1):
				print 'YLYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YLYL (num) VALUES (?)', (t,))
			if (current["sub"].find('ylyl') != -1):
				print 'YLYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YLYL (num) VALUES (?)', (t,))
			if (current["sub"].find('you laugh you lose') != -1):
				print 'YLYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YLYL (num) VALUES (?)', (t,))
			if (current["sub"].find('You Laugh You Lose') != -1):
				print 'YLYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YLYL (num) VALUES (?)', (t,))
			if (current["sub"].find('[as] style bumps') != -1):
				print '[wsg] Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO WSG (num) VALUES (?)', (t,))
			if (current["sub"].find('Come share an [experience] with us.') != -1):
				print '[wsg] Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO WSG (num) VALUES (?)', (t,))
			if (current["sub"].find('YGYL') != -1):
				print 'YGYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YGYL (num) VALUES (?)', (t,))
			if (current["sub"].find('ygyl') != -1):
				print 'YGYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YGYL (num) VALUES (?)', (t,))
			if (current["sub"].find('you groove you lose') != -1):
				print 'YGYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YGYL (num) VALUES (?)', (t,))
			if (current["sub"].find('You Groove You Lose') != -1):
				print 'YGYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YGYL (num) VALUES (?)', (t,))
			if (current["sub"].find('anime') != -1):
				print 'Anime Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO anime (num) VALUES (?)', (t,))
			if (current["sub"].find('Anime') != -1):
				print 'Anime Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO anime (num) VALUES (?)', (t,))
			if (current["sub"].find('Panda') != -1):
				print 'Coca-Cola polar bear Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO bear (num) VALUES (?)', (t,))
			if (current["sub"].find('panda') != -1):
				print 'Coca-Cola polar bear Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO bear (num) VALUES (?)', (t,))
			if (current["sub"].find('boomer') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["sub"].find('Boomer') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["sub"].find('boomers') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["sub"].find('Boomers') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["sub"].find('zoomer') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["sub"].find('zoomers') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["sub"].find('Zoomer') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["sub"].find('Zoomers') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["sub"].find('comfy') != -1):
				print 'Comfy Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO comfy (num) VALUES (?)', (t,))
			if (current["sub"].find('Comfy') != -1):
				print 'Comfy Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO comfy (num) VALUES (?)', (t,))
			if (current["sub"].find('feel') != -1):
				print 'Feels Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO feel (num) VALUES (?)', (t,))
			if (current["sub"].find('Feel') != -1):
				print 'Feels Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO feel (num) VALUES (?)', (t,))
			if (current["sub"].find('gondola') != -1):
				print 'Gondola Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO gondola (num) VALUES (?)', (t,))
			if (current["sub"].find('Gondola') != -1):
				print 'Gondola Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO gondola (num) VALUES (?)', (t,))
			if (current["sub"].find('idol') != -1):
				print 'Idol Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO idol (num) VALUES (?)', (t,))
			if (current["sub"].find('Idol') != -1):
				print 'Idol Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO idol (num) VALUES (?)', (t,))
			if (current["sub"].find('idols') != -1):
				print 'Idol Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO idol (num) VALUES (?)', (t,))
			if (current["sub"].find('Idols') != -1):
				print 'Idol Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO idol (num) VALUES (?)', (t,))
			if (current["sub"].find('Initial') != -1):
				print 'Initial D Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO initialD (num) VALUES (?)', (t,))
			if (current["sub"].find('initial') != -1):
				print 'Initial D Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO initialD (num) VALUES (?)', (t,))
			if (current["sub"].find('slav') != -1):
				print 'Slav Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO slav (num) VALUES (?)', (t,))
			if (current["sub"].find('Slav') != -1):
				print 'Slav Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO slav (num) VALUES (?)', (t,))
			if (current["sub"].find('toku') != -1):
				print 'Toku Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO toku (num) VALUES (?)', (t,))
			if (current["sub"].find('Toku') != -1):
				print 'Toku Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO toku (num) VALUES (?)', (t,))
			if (current["com"].find('YLYL') != -1):
				print 'YLYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YLYL (num) VALUES (?)', (t,))
			if (current["com"].find('ylyl') != -1):
				print 'YLYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YLYL (num) VALUES (?)', (t,))
			if (current["com"].find('you laugh you lose') != -1):
				print 'YLYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YLYL (num) VALUES (?)', (t,))
			if (current["com"].find('You Laugh You Lose') != -1):
				print 'YLYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YLYL (num) VALUES (?)', (t,))
			if (current["com"].find('WSG') != -1):
				print '[wsg] Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO WSG (num) VALUES (?)', (t,))
			if (current["com"].find('[as] style bumps') != -1):
				print '[wsg] Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO WSG (num) VALUES (?)', (t,))
			if (current["com"].find('Come share an [experience] with us.') != -1):
				print '[wsg] Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO WSG (num) VALUES (?)', (t,))
			if (current["com"].find('YGYL') != -1):
				print 'YGYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YGYL (num) VALUES (?)', (t,))
			if (current["com"].find('ygyl') != -1):
				print 'YGYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YGYL (num) VALUES (?)', (t,))
			if (current["com"].find('you groove you lose') != -1):
				print 'YGYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YGYL (num) VALUES (?)', (t,))
			if (current["com"].find('You Groove You Lose') != -1):
				print 'YGYL Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO YGYL (num) VALUES (?)', (t,))
			if (current["com"].find('anime') != -1):
				print 'Anime Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO anime (num) VALUES (?)', (t,))
			if (current["com"].find('Anime') != -1):
				print 'Anime Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO anime (num) VALUES (?)', (t,))
			if (current["com"].find('Panda') != -1):
				print 'Coca-Cola polar bear Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO bear (num) VALUES (?)', (t,))
			if (current["com"].find('panda') != -1):
				print 'Coca-Cola polar bear Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO bear (num) VALUES (?)', (t,))
			if (current["com"].find('boomer') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["com"].find('Boomer') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["com"].find('boomers') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["com"].find('Boomers') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["com"].find('zoomer') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["com"].find('zoomers') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["com"].find('Zoomer') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["com"].find('Zoomers') != -1):
				print 'Boomer Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO boomer (num) VALUES (?)', (t,))
			if (current["com"].find('comfy') != -1):
				print 'Comfy Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO comfy (num) VALUES (?)', (t,))
			if (current["com"].find('Comfy') != -1):
				print 'Comfy Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO comfy (num) VALUES (?)', (t,))
			if (current["com"].find('feel') != -1):
				print 'Feels Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO feel (num) VALUES (?)', (t,))
			if (current["com"].find('Feel') != -1):
				print 'Feels Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO feel (num) VALUES (?)', (t,))
			if (current["com"].find('gondola') != -1):
				print 'Gondola Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO gondola (num) VALUES (?)', (t,))
			if (current["com"].find('Gondola') != -1):
				print 'Gondola Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO gondola (num) VALUES (?)', (t,))
			if (current["com"].find('idol') != -1):
				print 'Idol Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO idol (num) VALUES (?)', (t,))
			if (current["com"].find('Idol') != -1):
				print 'Idol Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO idol (num) VALUES (?)', (t,))
			if (current["com"].find('idols') != -1):
				print 'Idol Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO idol (num) VALUES (?)', (t,))
			if (current["com"].find('Idols') != -1):
				print 'Idol Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO idol (num) VALUES (?)', (t,))
			if (current["com"].find('Initial') != -1):
				print 'Initial D Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO initialD (num) VALUES (?)', (t,))
			if (current["com"].find('initial') != -1):
				print 'Initial D Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO initialD (num) VALUES (?)', (t,))
			if (current["com"].find('slav') != -1):
				print 'Slav Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO slav (num) VALUES (?)', (t,))
			if (current["com"].find('Slav') != -1):
				print 'Slav Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO slav (num) VALUES (?)', (t,))
			if (current["com"].find('toku') != -1):
				print 'Toku Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO toku (num) VALUES (?)', (t,))
			if (current["com"].find('Toku') != -1):
				print 'Toku Thread found:', current["no"]
				t = current["no"]
				c.execute('INSERT INTO toku (num) VALUES (?)', (t,))
		except:
			pass
conn.commit()
db_message()
print "[DONE]"
