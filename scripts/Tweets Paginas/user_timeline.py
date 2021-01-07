import tweepy
import pymysql as MySQLdb
from time import sleep
import pandas as pd
import conexao


def get_user_timeline(api, username, user_fk):

	count = 200
	try:     
		# Creation of query method using parameters
		tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
		tweets = [[tweet.user.screen_name, tweet.text, tweet.created_at ]for tweet in tweets]

		for tweet in tweets:
		 	#print(f'{user_fk} - {tweet}')
			try:
				cursor.execute('INSERT INTO tweets_aleatorio (user_nome, tweet, user_fk, data) VALUES (%s, %s, %s, %s)', (tweet[0], tweet[1], user_fk, tweet[2]))
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

api = conexao.get_api()

#get_user_timeline(api, 'Montalvaooo')


con = conexao.get_mysql()
cursor = con.cursor()
sql = f"select * from user_aleatorio"
cursor.execute(sql)
consulta = cursor.fetchall()


for nome in consulta:

	pk_cod = nome[0]
	print('---')
	get_user_timeline(api, nome[1], pk_cod)


con.close()