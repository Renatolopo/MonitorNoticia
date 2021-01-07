import tweepy
import pymysql as MySQLdb


def get_api(stream=False):
	chave_consumidor = 'uvYDBa4HA6xSbGDVVLuL5kWWW'
	segredo_consumidor = 'RGyzZdfEjdMSm87109yiMyPqkaLYEN1ox0ogOQSaxENyU9ziq6'
	token_acesso = '2559540815-3OWEk9l7ImzsH9UP4ZVZ6aKgCwV94s6EdaodlQC'
	token_acesso_segredo = 'p6eZ7banSAdSt3mDd5TxyVLwD7me66HDSxGhyQjW2Iqk0'

	autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
	autenticacao.set_access_token(token_acesso, token_acesso_segredo)
	if stream:
		return autenticacao
	api = tweepy.API(autenticacao)
	return api

def get_mysql():
	con = MySQLdb.connect(host='localhost',
                         user='root',
                         password='renato20',
                         db='test')
	return con

print('Hello world')