import tweepy
import pymysql as MySQLdb


def get_api(stream=False):
	chave_consumidor = 'xx'
	segredo_consumidor = 'xx'
	token_acesso = 'xx-xx'
	token_acesso_segredo = 'xx'

	autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
	autenticacao.set_access_token(token_acesso, token_acesso_segredo)
	if stream:
		return autenticacao
	api = tweepy.API(autenticacao)
	return api

def get_mysql():
	con = MySQLdb.connect(host='xx',
                         user='xx',
                         password='xx',
                         db='Monitor_de_noticia')
	return con