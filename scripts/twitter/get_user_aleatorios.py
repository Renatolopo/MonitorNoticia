import conexao
import tweepy
from time import sleep

api = conexao.get_api(stream=True)

# Sobre escrevendo tweepy.StreamListener
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        #print(status.user.screen_name)
        set_database(status)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

def set_database(tweet):
	# cria conexão com o banco de dados
	con = conexao.get_mysql()
	cursor = con.cursor()

	try: 
		cursor.execute('INSERT INTO user_aleatorio (nome)\
			VALUES(%s)',(tweet.user.screen_name))
		print("Adicionado.....")
	except:
		# essa exceção acontece caso o tweet já exista na base de dados
		print('NÂO ADICIONADO*********')
	
	con.commit()
	con.close()

# Instanciando MyStreamListener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api, listener=myStreamListener)

# cordenadas do Brasil
location = [-73.09,-32.72,-33.98,4.09]

while True:
	try:
		myStream.filter( locations= location)
		print('Limite da API excedido')
		sleep(60 *20)	
	except:
		print('Erro aqui')
