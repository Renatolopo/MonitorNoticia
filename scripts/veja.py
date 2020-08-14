from bs4 import BeautifulSoup
import requests
import MySQLdb
from time import sleep

def getNoticia(noticia):
	titulo = noticia.h2.text
	descricao = noticia.find('span', class_ = 'description').text
	descricao = descricao.replace('\t','').replace('\n','')
	data = noticia.time.text.replace('| ','')
	
	titulo = str(titulo)
	data = str(data)
	descricao = str(descricao)
	if not descricao:
		descricao = '-' 

	return [titulo, descricao, data]

while True:
	con = MySQLdb.connect(host="xx", user="xx", passwd="xx", db="Monitor_de_noticias")
	con.select_db('Monitor_de_noticias')
	cursor = con.cursor()

	r = requests.get('https://veja.abril.com.br/blog/')
	soup = BeautifulSoup(r.content, 'html.parser')
	noticias = soup.find_all('div', attrs={'class':'card'})

	for noticia in noticias:
		row = getNoticia(noticia)
		try:
			cursor.execute('INSERT INTO veja (TITULO, DESCRICAO, HORARIO)\
			 VALUES (%s,%s,%s)',(row[0], row[1], row[2]))
			print('adicionado com sucesso')
		except:
			continue
	con.commit()
	con.close()
	sleep(10)