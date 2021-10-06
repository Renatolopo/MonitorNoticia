from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import MySQLdb
from time import sleep

def getCard(card):
	title = card.find_element_by_class_name('card-title').text
	subtitle = card.find_element_by_class_name('card-subtitle').text
	date = card.find_element_by_class_name('card-publish-date').text
	row = [title, subtitle, date]
	return row

while True:
	con = MySQLdb.connect(host="xx", user="xx", passwd="xx", db="Monitor_de_noticias")
	con.select_db('Monitor_de_noticias')
	cursor = con.cursor()

	option = Options()
	option.headless = True
	firefox = webdriver.Firefox(options=option)
	#url do sbt/jornalismo
	firefox.get('https://www.sbt.com.br/jornalismo')
	cards = firefox.find_elements_by_class_name('cards')
	for card in cards:
		row = getCard(card)
		try:
			cursor.execute('INSERT INTO Sbt (TITLE, SUBTITLE, PUBLISHED)\
				VALUES (%s,%s,%s)',(row[0],row[1],row[2]))
			print(f'adicionado com sucesso\n')
		except:
			#exeção gerada quando a noticia já existe no banco de dados
			continue
	con.commit()
	con.close()
	firefox.quit()
	sleep(60*3)