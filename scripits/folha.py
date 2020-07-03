import feedparser
from time import sleep
import pandas as pd

#retorna a linha com uma noticia e remove os caracteres ", ' , e \n
def getEntry(entry):
	row = [f'{entry.title}',f'|{entry.title_detail}',f'|{entry.links}',f'|{entry.link}',f'|{entry.summary}',f'|{entry.summary_detail}'\
	,f'|{entry.published}',f'|{entry.published_parsed}']
	for i in range(0,len(row)):
		row[i] =  row[i].replace("'", " ")
		row[i] =  row[i].replace('"', " ")
		row[i] =  row[i].replace('\n', " ")
	return row

def criaArquivo():
	fl = open('../output/folha.csv','w')
	fl.write('title |title_detail |links |link |summary |summary_detail |published |published_parsed\n')
	fl.close()
#escreve uma linha no arquivo
def setArquivo(row):
	fl = open('../output/folha.csv','a')
	for i in row:
		fl.write(i)
	fl.write('\n')
	fl.close()

#verifica se o titulo já existe no arquivo
def titleInFile(title):
	file = pd.read_csv('../output/folha.csv','r', delimiter = '|')
	file = file.values
	for i in file:
		if title in i:
			return True
	return False

criaArquivo()
cont = 0
while True:
	# feed RSS do folha de São paulo
	NewsFeed = feedparser.parse("https://feeds.folha.uol.com.br/emcimadahora/rss091.xml")
	for entry in NewsFeed.entries:
		row = getEntry(entry)
		title = row[0]
		if titleInFile(title):
			continue
		else:
			setArquivo(row)
			print(f'linha {cont} adicionada')
			cont += 1
	sleep(10)
