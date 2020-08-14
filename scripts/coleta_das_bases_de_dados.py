import pandas as pd
import sqlalchemy

def getConexao(drive, user, passwd, host, porta, db):
	return  sqlalchemy.create_engine(f'mysql+{drive}://{user}:{passwd}@{host}:{porta}/{db}')

def getDataBase(data_base, engine):
	return pd.read_sql_table(data_base,engine)
	 

engine = getConexao('xx', 'xx', 'xx', 'xx', 'xx', 'xx')
list_db = ['G1', 'Sbt', 'veja', 'R7', 'Folha', 'Twitter1']
df = dict()
for db in list_db:
	df[db] = getDataBase(db, engine)

print(df['Twitter1'])