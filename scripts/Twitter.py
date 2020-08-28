import tweepy
import MySQLdb

api_key = 'DkxBvaO3g3VxsEguC1jyv7USW'
api_key_secret = 'GbfVF3TvjOZcYTPjR4w4RoxSM1tjJMzJXEXBCxAxZNWnfPUPyw'
access_token = '2559540815-JAVBuM9UWAft9WED76vUNFnUXaKGFbO2UixK4WC'
access_token_secret = 'u4RycdCpGDG9uT3DJQNoGE7sWRPHRSuCtakF20x0Z4UrY'

autenticacao = tweepy.OAuthHandler(api_key, api_key_secret)
autenticacao.set_access_token(access_token, access_token_secret)
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
	try:
		resultados = twitter.search(q=name)

		for tweet in resultados:
			try: 
				cursor.execute('INSERT INTO Twitter (USUARIO, TWEET, DATA_TWEET)\
					VALUES(%s, %s, %s)',(tweet.user.screen_name, tweet.text, tweet.created_at))
				print("Adicionado.....")
			except:
				# essa exceção acontece caso o tweet já exista na base de dados
				print('NÂO ADICIONADO*********')
				continue

	except tweepy.error.RateLimitError:
		print('Limite de acesso da API atingido... aguarde')
		sleep(60 * 60)


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


