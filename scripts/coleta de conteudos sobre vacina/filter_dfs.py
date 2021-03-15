import getters as get
import pandas as pd 

def filter_vacine(noticia):
    p_noticia = noticia.split()
    for p in p_noticia:
        if p in vacinas:
            return True
    return False


vacinas = ["Vacina","vacina","vacinas","Vacinas","Ad26 SARS-CoV-2","mRNA 1273", "BNT162", "AZD1222", "CoronaVac", "AD5-nCov",
"NVX-CoV2373", "Sputnik V", "Covaxin", "vacinado", "vacinando", "vacinou","imunidade", "vacinara", "Astrazeneca"]

def filter_G1():
    df = get.get_df('G1')
    con = get.get_mysql()
    cursor = con.cursor()
    site = 'G1'
    for i in range(len(df.ID)):
        if filter_vacine(df["TITLE"].iloc[i]):
            link = df['LINK'].iloc[i]
            publishied = df['PUBLISHED'].iloc[i]
            title = df["TITLE"].iloc[i]

            try:
                cursor.execute('INSERT INTO noticia_vacina(title, link, publishied, site)\
                    VALUES(%s, %s, %s, %s)',(str(title), str(link), str(publishied), site))
                print(f'add...')
            except BaseException as e:
                print(e)
                continue

    print("FIM")
    con.commit()
    con.close()


    #print(df)

def filter_folha():
    df = get.get_df('Folha')
    con = get.get_mysql()
    cursor = con.cursor()
    site = 'Folha'
   
    for i in range(len(df.ID)):
        if filter_vacine(df["TITLE"].iloc[i]):
            link = df['LINK'].iloc[i]
            publishied = df['PUBLISHED'].iloc[i]
            title = df["TITLE"].iloc[i]

            try:
                cursor.execute('INSERT INTO noticia_vacina(title, link, publishied, site)\
                    VALUES(%s, %s, %s, %s)',(str(title), str(link), str(publishied), site))
                print(f'add...')
            except BaseException as e:
                print(e)
                continue

    print("FIM")
    con.commit()
    con.close()


def filter_tweets():
    df = get.get_df('tweet_paginas')
    con = get.get_mysql()
    cursor = con.cursor()

    for i in range(len(df.tweet)):
        if filter_vacine(df["tweet"].iloc[i]):
            pk_cod = df['pk_cod'].iloc[i]
            nome = df['nome'].iloc[i]
            tweet = df['tweet'].iloc[i]
            data = df['data'].iloc[i]
            id_tweet = df['id_tweet'].iloc[i]

            try:
                cursor.execute('INSERT INTO vacina_paginas_noticia(pk_cod, nome, tweet, data, id_tweet)\
                    VALUES(%s, %s, %s, %s, %s)',(str(pk_cod), str(nome), str(tweet), str(data), str(id_tweet)))
                print(f'add...')
            except BaseException as e:
                print(e)
                continue

    print("FIM")
    con.commit()
    con.close()
 
           


