import tweepy
import MySQLdb

chave_consumidor = 'xx'
segredo_consumidor = 'xx'
token_acesso = 'x-x'
token_acesso_segredo = 'xx'

autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso, token_acesso_segredo)
twitter = tweepy.API(autenticacao)


def getTrends():
	#Where On Earth ID para o Brasil é 23424768.
	BRAZIL_WOE_ID = 23424768	 
	brazil_trends = twitter.trends_place(BRAZIL_WOE_ID)
	tt = brazil_trends[0]
	list_trends = []
	for i in tt['trends']:
		list_trends.append(str(i['name']).strip("#"))

	return list_trends

def getTweets(name, cursor):
	print(f'Buscando por {name}....')
	resultados = twitter.search(q=name)

	for tweet in resultados:
		try: 
			cursor.execute('INSERT INTO Twitter1 (USUARIO, TWEET, DATA_TWEET)\
				VALUES(%s, %s, %s)',(tweet.user.screen_name, tweet.text, tweet.created_at))
			print("Adicionado.....")
		except:
			# essa exceção acontece caso o tweet já exista na base de dados
			print('NÂO ADICIONADO*********')
			continue


while True:
	con = MySQLdb.connect(host="xx", user="xx", passwd="xx", db="Monitor_de_noticias")
	con.select_db('Monitor_de_noticias')
	cursor = con.cursor()

	trends = getTrends()
	for trend in trends:
		print(trend)
		getTweets(trend, cursor)

	con.commit()
	con.close()


