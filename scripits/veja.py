from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep

#retorna a linha com uma noticia e remove os caracteres ", ', e \n.
def getNoticia(noticia):
	titulo = noticia.h2.text
	descricao = noticia.find('span', class_ = 'description').text
	descricao = descricao.replace('\t','').replace('\n','')
	data = noticia.time.text.replace('| ','')

	row = [f'{titulo}',f'|{descricao}',f'|{data}']
	for i in range(0,len(row)):
		row[i] =  row[i].replace("'", " ")
		row[i] =  row[i].replace('"', " ")
		row[i] =  row[i].replace('\n', " ")
	return row

def createFile():
	fl = open('../output/veja.csv','w')
	fl.write('Titulo |Descrição |Data\n')
	fl.close()
#escreve uma linha no arquivo
def setFile(row):
	fl = open('../output/veja.csv','a')
	for i in row:
		fl.write(i)
	fl.write('\n')
	fl.close()

#verifica se o titulo já existe no arquivo para não háver repetições.
def titleInFile(title):
	file = pd.read_csv('../output/veja.csv','r', delimiter = '|')
	file = file.values
	for i in file:
		if title in i:
			return True
	return False

createFile()
cont=0
while True:
	r = requests.get('https://veja.abril.com.br/blog/')
	soup = BeautifulSoup(r.content, 'html.parser')
	noticias = soup.find_all('div', attrs={'class':'card'})
	for noticia in noticias:
		row = getNoticia(noticia)
		title = row[0]
		if titleInFile(title):
			continue
		else:
			setFile(row)
			print(f'linha {cont} adicionada')
			cont += 1
	sleep(60)



