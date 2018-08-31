#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

def message():
	print "Clearing tables....        ",
c.execute('DELETE FROM WSG WHERE `_rowid_`')
print "Deleting all records and rows in WSG"
c.execute('DELETE FROM YGYL WHERE `_rowid_`')
print "Deleting all records and rows in YGYL"
c.execute('DELETE FROM YLYL WHERE `_rowid_`')
print "Deleting all records and rows in YLYL"
c.execute('DELETE FROM anime WHERE `_rowid_`')
print "Deleting all records and rows in anime"
c.execute('DELETE FROM bear WHERE `_rowid_`')
print "Deleting all records and rows in bear"
c.execute('DELETE FROM boomer WHERE `_rowid_`')
print "Deleting all records and rows in boomer"
c.execute('DELETE FROM comfy WHERE `_rowid_`')
print "Deleting all records and rows in comfy"
c.execute('DELETE FROM feel WHERE `_rowid_`')
print "Deleting all records and rows in feel"
c.execute('DELETE FROM gondola WHERE `_rowid_`')
print "Deleting all records and rows in gondola"
c.execute('DELETE FROM idol WHERE `_rowid_`')
print "Deleting all records and rows in idol"
c.execute('DELETE FROM initialD WHERE `_rowid_`')
print "Deleting all records and rows in initialD"
c.execute('DELETE FROM slav WHERE `_rowid_`')
print "Deleting all records and rows in slav"
c.execute('DELETE FROM sqlite_sequence WHERE `_rowid_`')
print "Deleting all records and rows in sqlite_sequence"
c.execute('DELETE FROM toku WHERE `_rowid_`')
print "Deleting all records and rows in toku"
conn.commit()
message()
print "[DONE]"