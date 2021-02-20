import feedparser
import requests
import MySQLdb
from time import sleep

def getEntry(entry):
	row =  [entry.title, entry.link, entry.summary, entry.published]
	return row

while True:
	con = MySQLdb.connect(host="xx", user="xx", passwd="xx", db="Monitor_de_noticias")
	con.select_db('Monitor_de_noticias')
	cursor = con.cursor()

	NewsFeed = feedparser.parse("http://g1.globo.com/dynamo/rss2.xml")
	for entry in NewsFeed.entries:
		row = getEntry(entry)
		try:
			cursor.execute('INSERT INTO G1 (TITLE, LINK, SUMMARY, PUBLISHED)\
			 VALUES (%s,%s,%s,%s)',(row[0], row[1], row[2], row[3]))
			print('adicionado com sucesso')
		except:
			#exeção gerada quando a noticia já existe no banco de dados
			continue
	con.commit()
	con.close()
	sleep(60 * 3)