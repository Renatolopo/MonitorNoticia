import getters as get 

import conexao
import tweepy
from time import sleep

api = conexao.get_api()
con = conexao.get_mysql()
cursor = con.cursor()

df = get.get_df('vacina_paginas_noticia')
ids_ainda_nao_coletados = get.get_dados_nao_inseridos()

for i in range(len(df)):
	id_tweet = df['id_tweet'].iloc[i]
	pk_cod = df['pk_cod'].iloc[i]
	
	if pk_cod in ids_ainda_nao_coletados:
		try:
			retweets = api.retweets(id=id_tweet, count=50)
			for rt in retweets:
				try:
					cursor.execute('INSERT INTO vacina_user_rt (nome, rt_em_fk) VALUES (%s, %s)', (str(rt.user.screen_name), str(pk_cod)))
					print('Adicionado')	

				except BaseException as e:
					# essa exceção acontece caso o usuário já exista na base de dados
					print(f'chave {pk_cod} - Não adicionado... Motivo {e}')
					continue
				con.commit()
		except tweepy.error.RateLimitError:
			print('Limite atingido...')
			sleep(60*15)
		except tweepy.error.TweepError:
			print(f'Chave {pk_cod} não existe mais...')
			continue
con.close()



