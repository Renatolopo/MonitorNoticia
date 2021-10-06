import tweepy
import pymysql as MySQLdb
from time import sleep

# Sobre escrevendo tweepy.StreamListener
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

# Inserir no banco de dados
def set_database(tweet):
	# cria conexão com o banco de dados
	con = MySQLdb.connect(host="200.131.5.71", user="renato", passwd="renato20", db="Monitor_de_noticia")
	cursor = con.cursor()

	try: 
		cursor.execute('INSERT INTO Twitter_streaming (USUARIO, TWEET, DATA_TWEET)\
			VALUES(%s, %s, %s)',(tweet.user.screen_name, tweet.text, tweet.created_at))
		print("Adicionado.....")
	except:
		# essa exceção acontece caso o tweet já exista na base de dados
		print('NÂO ADICIONADO*********')
	
	con.commit()
	con.close()



# credenciais
chave_consumidor = 'xx'
segredo_consumidor = 'xx'
token_acesso = 'x-x'
token_acesso_segredo = 'xx'

# criando uma autenticação
autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso, token_acesso_segredo)


# Instanciando MyStreamListener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = autenticacao, listener=myStreamListener)

# cordenadas do Brasil
location = [-73.09,-32.72,-33.98,4.09]

while True:
	try:
		myStream.filter( locations= location)
		print('Limite da API excedido')
		sleep(60 *20)	
	except:
		print('Erro aqui')

	