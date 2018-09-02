#!/usr/bin/env python

import sqlite3
import requests
import re
import os
import shutil

#connect to the db
conn = sqlite3.connect('database.db')
c = conn.cursor()

#counts how many rows there are in the table then converts it to something range can work with
c.execute('SELECT Count(*) FROM YLYL')
h = c.fetchone()
x = "".join([str(i) for i in h])	
y = int(x)

#goes through every row in the table
for i in range(1, y+1):
	content = 'YLYL'
	c.execute('SELECT num FROM YLYL WHERE ID=(?)', (i,))
	r = c.fetchone()
#formatting
	l = "".join([str(b) for b in r])
#build URL
	url = 'https://boards.4chan.org/wsg/thread/'+l+'/'
	print 'Grabbing '+content+' thread ID: '+l
#Download page
	r = requests.get(url)
#Error handling
	if r.status_code != 200 or not r.content :
		print 'Failed to read thread ID:', l
#Find all images in thread
	m = re.findall(r'href=".*?(\/\/i.4cdn.org/wsg\/[0-9]+.(webm))"', r.content)
	images = []
	for i in m :
		images.append(i[0])
	print 'Found '+str(len(images))+' webms'
if not os.path.exists(content) :
	os.makedirs(content)
for image in images :
	match = re.findall(r'\/([0-9]+.(webm))$', image)
	if match[0] :
		filename = content+'/'+match[0][0]
		print 'Downloading /'+filename
	q = requests.get('https:'+image, stream=True)
	with open(filename, 'wb') as f :
		q.raw.decode_content = True
		shutil.copyfileobj(q.raw, f)