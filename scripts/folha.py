import feedparser
import requests
import MySQLdb
from time import sleep

def getEntry(entry):
	try: 
		row = [entry.title, entry.link, entry.summary, entry.published]
	except:
		row = ['null','null','null', 'null']
	return row

while True:
	con = MySQLdb.connect(host="xx", user="xx", passwd="xx", db="Monitor_de_noticias")
	con.select_db('Monitor_de_noticias')
	cursor = con.cursor()

	Newsfeed = feedparser.parse('https://feeds.folha.uol.com.br/emcimadahora/rss091.xml')
	for entry in Newsfeed.entries:
		row = getEntry(entry)
		try:
			cursor.execute('INSERT INTO Folha (TITLE, LINK, SUMMARY,PUBLISHED)\
				VALUES (%s,%s,%s,%s)',(row[0],row[1],row[2],row[3]))
			print(f'adicionado com sucesso\n')
		except:
			continue
	con.commit()
	con.close()
	sleep(10)