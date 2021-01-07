import tweepy
import conexao
from time import sleep

api = conexao.get_api()
con = conexao.get_mysql()
cursor = con.cursor()

username = 'portalR7'


count = 100
try:     
	# Creation of query method using parameters
	tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
	tweets = [[tweet.user.screen_name, tweet.text, tweet.created_at, tweet.id]for tweet in tweets]

	for tweet in tweets:
		#print(f'{tweet}')
		try:
			cursor.execute('INSERT INTO tweet_paginas (nome, tweet, data, id_tweet) VALUES (%s, %s, %s, %s)', (tweet[0], tweet[1], tweet[2], tweet[3]))
			print('Adicionado')
		except:
			# essa exceção acontece caso o usuário já exista na base de dados
			print('Não adicionado')
			continue
		con.commit()
	 
except tweepy.error.RateLimitError:
	print('RateLimitError aguardando...')
	sleep(10*60)

except BaseException as e:
	print('failed on_status,',str(e))
	sleep(3)