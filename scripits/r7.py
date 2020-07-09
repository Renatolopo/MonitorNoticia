import feedparser
import requests
import MySQLdb
from time import sleep

def getEntry(entry):
	row =  [entry.title, entry.link, entry.summary, entry.published]
	return row

while True:
	con = MySQLdb.connect(host="servidor", user="usuario", passwd="senha", db="base de dados")
	con.select_db('base de dados')
	cursor = con.cursor()

	NewsFeed = feedparser.parse("https://noticias.r7.com/feed.xml")
	for entry in NewsFeed.entries:
		row = getEntry(entry)
		try:
			cursor.execute('INSERT INTO R7 (TITLE, LINK, SUMMARY, PUBLISHED)\
			 VALUES (%s,%s,%s,%s)',(row[0], row[1], row[2], row[3]))
			print('adicionado com sucesso')
		except:
			continue
	con.commit()
	con.close()
	sleep(120)