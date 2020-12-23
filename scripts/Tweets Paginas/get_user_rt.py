import conexao

api = conexao.get_api()
con = conexao.get_mysql()
cursor = con.cursor()

sql = "select pk_cod, nome, id_tweet from tweet_paginas where pk_cod > 1446 and nome!= 'g1'"
cursor.execute(sql)
consulta = cursor.fetchall()
for tupla in consulta:
	#print(tupla)


	id_tweet = tupla[2]
	pk_cod = tupla[0]
	fonte = tupla[1]


	retweets = api.retweets(id=id_tweet, count=100)
	for rt in retweets:
		#print(rt.user.screen_name)
		try:
			cursor.execute('INSERT INTO user_rt (nome, rt_em_fk) VALUES (%s, %s)', (rt.user.screen_name, pk_cod))
			print('Adicionado')
		except:
			# essa exceção acontece caso o usuário já exista na base de dados
			print('Não adicionado')
			continue
		con.commit()
con.close()



