import conexao

api = conexao.get_api()
con = conexao.get_mysql()
cursor = con.cursor()

sql = "select pk_cod, nome, id_tweet from tweet_paginas where pk_cod > 4331 and (nome = 'sbtjornalismo' or nome = 'portalR7')"
cursor.execute(sql)
consulta = cursor.fetchall()
for tupla in consulta:
	id_tweet = tupla[2]
	pk_cod = tupla[0]
	fonte = tupla[1]


	retweets = api.retweets(id=id_tweet, count=50)
	for rt in retweets:
		try:
			cursor.execute('INSERT INTO user_rt (nome, rt_em_fk) VALUES (%s, %s)', (rt.user.screen_name, pk_cod))
			print('Adicionado')
		except BaseException as e:
			# essa exceção acontece caso o usuário já exista na base de dados
			print(f'chave {pk_cod} - Não adicionado... Motivo {e}')
			continue
		con.commit()
con.close()



