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
  
