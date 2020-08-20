import pandas as pd
import mysql.connector

def getConexao():
	return  mysql.connector.connect(
        user="xx",
        host="xx",
        database="xx",
        password='xx',
    )


def getDataBase(data_base, con):
	return pd.read_sql(f'select * from {data_base};', con=con) 
	 

con = getConexao()
list_db = ['G1', 'Sbt', 'veja', 'R7', 'Folha', 'Twitter']
df = dict()
for db in list_db:
	df[db] = getDataBase(db, con)

print(df['Twitter1'])

con.close()


