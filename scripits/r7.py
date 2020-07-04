import feedparser
from time import sleep
import pandas as pd

#retorna a linha com uma noticia e remove os caracteres ", ', e \n.
def getEntry(entry):
	row = [f'{entry.id}',f'|{entry.guidislink}',f'|{entry.link}',f'|{entry.published}',f'|{entry.published_parsed}',f'|{entry.updated}'\
	,f'|{entry.updated_parsed}',f'|{entry.links}',f'|{entry.href}',f'|{entry.title}',f'|{entry.title_detail}',f'|{entry.summary}'\
	,f'|{entry.summary_detail}',f'|{entry.content}',f'|{entry.mediaurl}',f'|{entry.mediasource}',f'|{entry.authors}'\
	,f'|{entry.author_detail}',f'|{entry.author}']
	for i in range(0, len(row)):
		row[i] =  row[i].replace("'", " ")
		row[i] =  row[i].replace('"', " ")
		row[i] =  row[i].replace('\n', " ")
	return row

def criaArquivo():
	fl = open('../output/r7.csv','w')
	fl.write('id |guidislink |link |published |published_parsed |updated |updated_parsed |links |href |title |title_detail \
		|summary |summary_detail |content |mediaurl |mediasource |authors |author_detail |author\n')
	fl.close()

#escreve uma linha no arquivo.
def setArquivo(row):
	fl = open('../output/r7.csv', 'a')
	for i in row:
		fl.write(i)
	fl.write('\n')
	fl.close()

#verifica se o titulo já existe no arquivo para não repetir uma mesma noticia.
def titleInFile(title):
	file = pd.read_csv('../output/r7.csv','r',delimiter='|')
	file = file.values
	for i in file:
		if title in i:
			return True
	return False


criaArquivo()
cont = 0
while True:
	#feed RSS do site R7.
	NewsFeed = feedparser.parse("https://noticias.r7.com/feed.xml")
	for entry in NewsFeed.entries:
		row = getEntry(entry)
		title = row[9].replace('|','')
		if titleInFile(title):
			continue
		else:
			setArquivo(row)
			print(f'linha {cont} adicionada')
			cont += 1
	sleep(60)
