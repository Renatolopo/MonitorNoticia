import pandas as pd
import pymysql as MySQLdb


def get_mysql():
	con = MySQLdb.connect(host='xx',
                         user='xx',
                         password='xx',
                         db='Monitor_de_noticia')
	return con



def get_df(name, limit=None):
    if limit:
        return pd.read_sql(f'select * from {name} where pk_cod > {limit};', con= get_mysql()) 
    else:
        return pd.read_sql(f'select * from {name};', con= get_mysql()) 


def get_noticias(site):
    return pd.read_sql(f"select * from noticia_vacina where id > 3692 and site = '{site}';", con= get_mysql())


def get_dados_nao_inseridos(site=None):
    con = get_mysql()
    cursor = con.cursor()
    cursor.execute('use Monitor_de_noticia;')
    
    if site:
        cursor.execute(f"select * from noticia_vacina where site = '{site}';")
        noticia_vacina = cursor.fetchall()
        noticia_vacina = [x for x in noticia_vacina]

        cursor.execute(f"select * from comentario_vacina where site = '{site}';")
        comentario_vacina = cursor.fetchall()
        ids_ja_inseridos = [x[0] for x in comentario_vacina]
        

        nao_inseridos = [x[0] for x in noticia_vacina if x[0] not in ids_ja_inseridos]
        return nao_inseridos

    else:
        cursor.execute(f"select * from vacina_paginas_noticia;")
        noticia_vacina = cursor.fetchall()
        noticia_vacina = [x for x in noticia_vacina]

        cursor.execute(f"select * from vacina_user_rt;")
        rt = cursor.fetchall()
        ids_ja_inseridos = [x[2] for x in rt]
        

        nao_inseridos = [x[0] for x in noticia_vacina if x[0] not in ids_ja_inseridos]
        return nao_inseridos