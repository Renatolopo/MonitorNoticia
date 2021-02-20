import tweepy
import pymysql as MySQLdb


def get_api(stream=False):
	chave_consumidor = 'x'
	segredo_consumidor = 'x'
	token_acesso = 'x-x'
	token_acesso_segredo = 'x'

	autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
	autenticacao.set_access_token(token_acesso, token_acesso_segredo)
	if stream:
		return autenticacao
	api = tweepy.API(autenticacao)
	return api

def get_mysql():
	con = MySQLdb.connect(host='localhost',
                         user='root',
                         password='',
                         db='test')
	return con

