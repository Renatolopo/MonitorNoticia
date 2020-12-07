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
			followers = twitter.followers(screen_name=pag)
			for follower in followers:
				print('==='*15)
				
				try:
			
					user_timeline = twitter.user_timeline(screen_name=f'@{follower.screen_name}')
					for publi in user_timeline:
						print(f'{pag}\nname: {follower.screen_name} \npubli: {publi.text} \n\n')


				except tweepy.error.RateLimitError:
					erro_limite()

		except tweepy.error.RateLimitError:
			erro_limite()
