import pandas as pd 
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
import numpy as np

def get_noticias():
	list_db = ['G1', 'Sbt', 'veja', 'R7', 'Folha']
	list_column = [ 'TITLE', 'TITULO', 'SUMMARY', 'SUBTITLE', 'DESCRICAO']

	dfs = []
	for db in list_db:
		df = pd.read_csv(f'../Dados coletados/{db}.csv')
		columns_drop = [x for x in df.columns if x not in list_column]
		df = df.drop(columns=columns_drop)
		df.columns = ['TITLE', 'SUMMARY']

		print(db)
		print(df.shape)
		dfs.append(df)
	df = pd.concat(dfs)
	print(df)
	df.to_csv('../Dados coletados/todos_sites.csv')


def getLanguage(text):
	languages_ratios = {}
	tokens = wordpunct_tokenize(text)
	words = [word.lower() for word in tokens]
	for language in stopwords.fileids():
		stopwords_set = set(stopwords.words(language))
		words_set = set(words)
		common_elements = words_set.intersection(stopwords_set)
		languages_ratios[language] = len(common_elements) # language "score"

	if languages_ratios[(max(languages_ratios, key=languages_ratios.get))] == 0:
		return 'Não identificado'

	return str(max(languages_ratios, key=languages_ratios.get))

def get_twiter():
	df = pd.read_csv('../Dados coletados/Twitter.csv',encoding='utf-8',  lineterminator='\n')

	#df = pd.read_csv(open('../Dados coletados/Twitter.csv','rU'), encoding='utf-8', engine='c')
	df['language'] = df['TWEET'].map(getLanguage)
	print(df)
	print('\n\n')
	print(df.groupby(by='language').size())

	df = df[df['language'] == 'portuguese']
	print(df)
	df.to_csv('../Dados coletados/Twitter_padronizado.csv')

#get_twiter()
get_noticias()