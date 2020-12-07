import tweepy
import pymysql as MySQLdb
from time import sleep


def erro_limite():
	print('Limite de acesso da API atingido... aguarde')
	sleep(60 * 3)


chave_consumidor = 'uvYDBa4HA6xSbGDVVLuL5kWWW'
segredo_consumidor = 'RGyzZdfEjdMSm87109yiMyPqkaLYEN1ox0ogOQSaxENyU9ziq6'
token_acesso = '2559540815-3OWEk9l7ImzsH9UP4ZVZ6aKgCwV94s6EdaodlQC'
token_acesso_segredo = 'p6eZ7banSAdSt3mDd5TxyVLwD7me66HDSxGhyQjW2Iqk0'

autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso, token_acesso_segredo)
twitter = tweepy.API(autenticacao)


while True:
	paginas = ['@G1','@sbtjornalismo','@VEJA','@folha','@portalR7']
	for pag in paginas:
		try:
			resultados = twitter.user_timeline(screen_name=pag)
			for tweet in resultados:
				print('==='*15)
				print(f'{tweet.text}\n')
				try:
					retweets = twitter.retweets(tweet.id)
					for rt in retweets:
						try:
							user_timeline = twitter.user_timeline(screen_name=f'@{rt.user.screen_name}')
							for publi in user_timeline:
								print(f'{pag}\nname: {rt.user.screen_name} \npubli: {publi.text} \nref_id: {tweet.id}\n')

						except tweepy.error.RateLimitError:
							erro_limite()


				except tweepy.error.RateLimitError:
					erro_limite()

		except tweepy.error.RateLimitError:
			erro_limite()



# tweet_noticia(id_tweet,tweet,user,data)
# user_rt(id_tweet,tweet_que_deu_rt,tweet,user,data)


# http://docs.tweepy.org/en/v3.5.0/api.html
# https://www.geeksforgeeks.org/python-status-object-in-tweepy/
# https://gist.github.com/marcoscastro/bc43e1741b4af47fda0ef289093aae01
# https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
