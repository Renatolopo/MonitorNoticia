import tweepy
import pymysql as MySQLdb
from time import sleep
import conexao


def erro_limite():
	print('Limite de acesso da API atingido... aguarde')
	sleep(60 * 3)


api = conexao.get_api()
con = conexao.get_mysql()
cursor = con.cursor()

while True:
	paginas = ['@G1','@sbtjornalismo','@VEJA','@folha','@portalR7']
	for pag in paginas:
		try:
			resultados = api.user_timeline(screen_name=pag)
			for tweet in resultados:
				try:
					cursor.execute('INSERT INTO tweet_paginas (nome, tweet, data, id_tweet) VALUES (%s, %s, %s, %s)', (tweet.user.screen_name, tweet.text, tweet.created_at, tweet.id))
					print('Adicionado')
				except:
					# essa exceção acontece caso o usuário já exista na base de dados
					print('Não adicionado')
					continue
				con.commit()


		except tweepy.error.RateLimitError:
			erro_limite()
	sleep(5*60)# aguarda 5 min para as paginas atualizar o feed

con.close()



# http://docs.tweepy.org/en/v3.5.0/api.html
# https://www.geeksforgeeks.org/python-status-object-in-tweepy/
# https://gist.github.com/marcoscastro/bc43e1741b4af47fda0ef289093aae01
# https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
