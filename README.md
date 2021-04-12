# MonitorNoticia
## Coleta dos dados
* Bibliotecas necessárias:
  - selenium
  - feedparser
  - requests
  - tweepy
  - bs4
  
  - MySQLdb
  - mysql.connector
  - pandas
  
  As demais já vem por padrão no python.
  
  
* Drivers
   - O driver a ser usado pelo firefox é o geckodriver, tem a versão 0.26 e 0.27
   para o caso de incompatibilidade. O chromedriver só será necessário caso recorra 
   ao navegador google chrome. 
  - O driver que for ser usado precisa ser extraido e colocado no $PATH da sua maquina ou passado 
  como parametro o caminho onde ele se encontra na hora de chamar o construtor do webdriver no script.
  
  
  ## Scripts
  ### Web Scraping
  [Site do G1](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/G1.py)
  
  [Comentarios das noticias do G1](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/comentarios_g1.py)
  
  [Site do Folha de São Paulo](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/folha.py)
  
  [Site do R7](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/r7.py)
  
  [Site do Sbt](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/sbt.py)
  
  [Site da Revista Veja](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/veja.py)
  
  
  ### Twitter
  [get_followers_pag](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/get_followers_pag.py) - Coleta os seguidores de uma pagina específica.
  
  [get_pag_twitter](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/get_pag_twitter.py) -  Coleta Tweets dos perfis '@G1', '@sbtjornalismo', '@VEJA',' @folha', '@portalR7'.
  
  [get_user_aleatorios](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/get_user_aleatorios.py) - coleta nome de usuários do Twitter baseado em publicações feita em tempo real.
  
  [get_user_rt](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/get_user_rt.py) - coleta o nome de usuários que deram RT em uma publicação.
  
  [streaming_tweets](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/streaming_tweets.py) - coleta tweets em tempo real que são publicados no territorio Brasileiro.
  
  [user_timeline](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/user_timeline.py) - coleta tweets da timeline de um usuário.
  
  [tweets_trendig_topics](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/tweets_trendig-topics.py) - coleta tweets pesquisando pelos termos que estão nos trending topics.
  

  
  
