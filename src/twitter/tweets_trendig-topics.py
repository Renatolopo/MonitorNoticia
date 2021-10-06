import tweepy
import pymysql as MySQLdb
from time import sleep


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
	try:
		resultados = twitter.search(q=name, lang='pt')

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
		sleep(60 * 3)

	

while True:
	con = MySQLdb.connect(host="200.131.5.71", user="renato", passwd="renato20", db="Monitor_de_noticia")
	cursor = con.cursor()
	cont = 0

	trends = getTrends()
	for trend in trends:
		print(trend)
		cont += 1
		print(f'busca: {cont}')
		getTweets(trend, cursor,)


		con.commit()
	con.close()
	print('*********************************************************************************')
