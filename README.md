# MonitorNoticia
[![GitHub](https://img.shields.io/github/license/Renatolopo/MonitorNoticia)](https://github.com/Renatolopo/MonitorNoticia/blob/master/LICENSE)

# Sobre o Projeto
Este trabalho propõe uma ferramenta para monitorar o que é publicado no país, seja na grande mídia ou seja nas redes sociais, neste trabalho será considerado a rede social Twitter e cinco sites de tradicionais veículos de comunicação, sendo eles G1, SBT, R7, revista Veja e Jornal Folha de São Paulo. A definição dos sites que foram monitorados neste trabalho se baseou em sistematizações promovidas pelo projeto [Media Ownership Monitor Brasil](http://brazil.mom-rsf.org/br/). Com a ferramenta proposta será possível observar  tendências na sociedade, preferências dos veículos de comunicação, repercussão de eventos na grande mídia e no Twitter, características das notícias da grande mídia e padrões de postagens no Twitter, entre outras possibilidades.

Este Repositório está disponibilizando os scripts de coleta e analise de dados usados no Projeto de Pesquisa "MONITOR DE NOTÍCIAS: SISTEMA PARA ANALISAR CONTEÚDOS PUBLICADOS EM SITES DA GRANDE MÍDIA E NA REDE SOCIAL TWITTER NO CONTEXTO BRASILEIRO" Feito por [Renato Lopo](https://github.com/Renatolopo) no IFNMG campus Januária.

## Coleta dos dados
 Os dados foram  coletados fazendo  web scraping com selenium e BeautifulSoup, leitura de feed RSS e utilizando a API do Twitter.

  ## Scripts
  Os scripts feito neste trabalho podem ser facilmente adaptados.
  ### Web Scraping e RSS
  Os scripts linkados a seguir foram utilizados para coletar as publicações dos sites de noticias e armazenar em um Banco de dados

  [G1](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/G1.py)  utiliza leitura de feed RSS.
  
  [Folha de São Paulo](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/folha.py) utiliza leitura de feed RSS.
  
  [R7](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/r7.py) utiliza leitura de feed RSS.
  
  [Sbt](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/sbt.py) utiliza web scraping com o selenium.
  
  [Revista Veja](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/web-scraping-paginas-de-noticias/veja.py) utiliza web scraping com o BeautifulSoup.
  
  
  ### Twitter
  Os scripts a seguir usa a API do Twitter junto com a biblioteca tweepy do Python para coletar tweets especificos ou usuários especificos e armazenar em um Banco de Dados.
  [get_followers_pag](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/get_followers_pag.py) - Coleta os seguidores de uma pagina específica.
  
  [get_pag_twitter](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/get_pag_twitter.py) -  Coleta Tweets dos perfis '@G1', '@sbtjornalismo', '@VEJA',' @folha', '@portalR7'.
  
  [get_user_aleatorios](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/get_user_aleatorios.py) - coleta nome de usuários do Twitter baseado em publicações feita em tempo real.
  
  [get_user_rt](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/get_user_rt.py) - coleta o nome de usuários que deram RT em uma publicação.
  
  [streaming_tweets](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/streaming_tweets.py) - coleta tweets em tempo real que são publicados no territorio Brasileiro.
  
  [user_timeline](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/user_timeline.py) - coleta tweets da timeline de um usuário.
  
  [tweets_trendig_topics](https://github.com/Renatolopo/MonitorNoticia/blob/master/scripts/twitter/tweets_trendig-topics.py) - coleta tweets pesquisando pelos termos que estão nos trending topics.
  

---- 
#### principais Bibliotecas utilizadas:
  - selenium
  - feedparser
  - requests
  - tweepy
  - bs4
  - MySQLdb
  - mysql.connector
  - pandas

  
  
#### Drivers
Para utilizar o selenium e nescessário utilizar web drivers para conectar com um navegador. Neste Projeto foi utilizado o geckodriver um driver do mozilla FireFox disponivel em https://github.com/mozilla/geckodriver/releases.

  
