import tweepy
import pymysql as MySQLdb
from time import sleep
import pandas as pd
import conexao


def erro_limite():
	print('Limite de acesso da API atingido... aguarde')
	sleep(60 * 3)


api = conexao.get_api()

# conexão Mysql
con = conexao.get_mysql()
cursor = con.cursor()

# paginas = ['@G1','@sbtjornalismo','@VEJA','@folha','@portalR7']
pag = '@sbtjornalismo'
count=500

try:
	followers = tweepy.Cursor(api.followers,screen_name=pag).items(count)
			 

	for follower in followers:
		try:
			cursor.execute('INSERT INTO user_follow (nome, segue) VALUES (%s, %s)', (follower.screen_name, pag))
			print('Adicionado')
		except:
			# essa exceção acontece caso o usuário já exista na base de dados
			print('Não adicionado')
			continue
		con.commit()
	
except BaseException as e:
	      print('failed on_status,',str(e))
	      sleep(3)

con.close()

