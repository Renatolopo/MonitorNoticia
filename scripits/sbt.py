from selenium import webdriver
from time import sleep
import pandas as pd

#retorna uma linha com a noticia e remove os caracteres ", ', e \n.
def getCard(card):
	title = card.find_element_by_class_name('card-title').text
	subtitle = card.find_element_by_class_name('card-subtitle').text
	date = card.find_element_by_class_name('card-publish-date').text
	row = [f'{title}',f'|{subtitle}',f'|{date}']
	for i in range(0,len(row)):
		row[i] = row[i].replace("'", " ")
		row[i] = row[i].replace('"', " ")
		row[i] = row[i].replace('\n', " ")
	return row

def createFile():
	fl = open('../output/sbt.csv','w')
	fl.write('title |subtitle |data\n')
	fl.close()
#escreve uma linha no arquivo.
def setFile(row):
	fl = open('../output/sbt.csv', 'a')
	for i in row:
		fl.write(i)
	fl.write('\n')
	fl.close()
#verifica se há titulo semelhante para não repetir
def titleInFile(title):
	file = pd.read_csv('../output/sbt.csv','r',delimiter='|')
	file = file.values
	for i in file:
		if title in i:
			return True
	return False

createFile()
cont = 0

while True:
	firefox = webdriver.Firefox()
	#url do sbt/jornalismo
	firefox.get('https://www.sbt.com.br/jornalismo ')
	cards = firefox.find_elements_by_class_name('cards')
	for card in cards:
		row = getCard(card)
		title = row[0]
		if titleInFile(title):
			continue
		else:
			setFile(row)
			print(f"linha {cont} adicionada")
			cont += 1
	firefox.quit()
	sleep(30)
	
