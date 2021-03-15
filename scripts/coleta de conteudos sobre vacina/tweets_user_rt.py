import tweepy
import pymysql as MySQLdb
from time import sleep
import pandas as pd
import conexao


def get_user_rt():
    con = conexao.get_mysql()
    cursor = con.cursor()

    sql = "use Monitor_de_noticia"
    cursor.execute(sql)
    sql = "select * from vacina_user_rt"
    cursor.execute(sql)
    consulta = cursor.fetchall()
    user_rt = [x for x in consulta]

    sql = "select user_nome from vacina_tweets_rt group by user_nome"
    cursor.execute(sql)
    consulta = cursor.fetchall()
    tweets_rt = [x[0] for x in consulta]


    user = [x for x in user_rt if x[1] not in tweets_rt] 

    return user
   


def get_user_timeline_rt(api, username, user_fk):

    count = 220
    try:     
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
        tweets = [[tweet.user.screen_name, tweet.text, tweet.created_at ]for tweet in tweets]

        for tweet in tweets:
          
            try:
                cursor.execute('INSERT INTO vacina_tweets_rt (user_nome, tweet, user_fk, data) VALUES (%s, %s, %s, %s)', (tweet[0], str(tweet[1]), user_fk, tweet[2]))
                print('Adicionado')
            except BaseException as e:
                # essa exceção acontece caso o usuário já exista na base de dados
                print(f'Não adicionado... Motivo {e}')
                continue
            con.commit()

    except tweepy.error.RateLimitError:
        print('RateLimitError aguardando...')
        sleep(10*60)

    except BaseException as e:
          print('failed on_status,',str(e))
          sleep(3)

api = conexao.get_api()

con = conexao.get_mysql()
cursor = con.cursor()
sql = f"use Monitor_de_noticia"
cursor.execute(sql)


user = get_user_rt()

for nome in user:
    pk_cod = nome[0]
    print('---')
    get_user_timeline_rt(api, nome[1], pk_cod)

con.close()