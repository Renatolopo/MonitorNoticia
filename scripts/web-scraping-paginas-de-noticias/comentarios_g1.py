from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests
import re


def scrapy_g1(page):
    driver.get(page)
    sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    
    comentarios = driver.find_elements_by_id('tabPane-COMMENTS')
    html = comentarios[0].get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')
    comentarios = soup.find_all('div', attrs = {'class':'Box-root-acb8bd0953d79380f99868ba1e9c06f2 HorizontalGutter-root-42028c0a7886c844bb9f01763cc43000 AllCommentsTabContainer-borderedComment-9cace0e311b29ae7445c79ba1d7c6378 HorizontalGutter-full-680598106a6954360bcd94b9d3839ca7'})


    for comentario in comentarios:
        content =  comentario.find('div', class_ = 'HTMLContent-root-5770ce4668399900d87c06ad10ba71a5 htmlContent-root-fe3506b39eaecd1a685ceda5e1292c4d coral coral-content coral-comment-content')
        print(f'- {content.text}\n')


def get_page(noticia):
    driver.get(noticia)
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    tag = driver.find_elements_by_id('boxComentarios')
    iframe = tag[0].get_attribute('innerHTML').split()
    link = iframe[1]
    link = re.sub('src=','',link)
    link = re.sub('"','',link)
    return link



lista_noticias = ['https://g1.globo.com/rj/rio-de-janeiro/noticia/2021/02/15/postes-de-iluminacao-em-mau-estado-de-conservacao-colocam-em-risco-a-vida-da-populacao.ghtml',
   'https://g1.globo.com/mg/minas-gerais/noticia/2021/02/15/covid-19-policia-civil-pericia-possivel-pane-eletrica-em-refrigerador-da-policlinica-de-igarape-com-centenas-de-vacinas.ghtml',
   'https://g1.globo.com/economia/noticia/2021/02/15/nigeriana-okonjo-iweala-torna-se-a-primeira-mulher-presidente-da-omc.ghtml',
   'https://g1.globo.com/df/distrito-federal/noticia/2021/02/15/justica-federal-nega-pedido-de-pensao-especial-para-tetranetos-de-tiradentes.ghtml',
   'https://g1.globo.com/rj/rio-de-janeiro/noticia/2021/02/15/imagens-mostram-idosos-recebendo-falsa-aplicacao-de-vacina-contra-a-covid-19-no-rj.ghtml',
   'https://g1.globo.com/bemestar/vacina/noticia/2021/02/15/oms-uso-emergencial-da-vacina-de-oxford.ghtml',
   'https://g1.globo.com/mg/minas-gerais/noticia/2021/02/15/covid-19-policia-civil-pericia-possivel-pane-eletrica-em-refrigerador-da-policlinica-de-igarape-com-centenas-de-vacinas.ghtml']

option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=r'./geckodriver')
for noticia in lista_noticias:
    page = get_page(noticia)
    scrapy_g1(page)

driver.close()
