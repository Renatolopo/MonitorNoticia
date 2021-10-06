from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests
import re
import filter_dfs
import getters as get

def insert_in_bd(comentario, pk_id, site):
    con = get.get_mysql()
    cursor = con.cursor()
    try:
        cursor.execute('INSERT INTO comentario_vacina(fk_id, comentario, site)\
            VALUES(%s, %s, %s)',(str(pk_id), str(comentario), str(site)))
        print(f'add...')
    except BaseException as e:
        print(e)

    con.commit()
    con.close()


def scrapy_g1(page, pk_id, site):
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
        if content:
            insert_in_bd(content.text, pk_id, site)


def get_page(noticia):
    driver.get(noticia)
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(5)
    tag = driver.find_elements_by_id('boxComentarios')
    try:
        iframe = tag[0].get_attribute('innerHTML').split()
        try:
            link = iframe[1]
            link = re.sub('src=','',link)
            link = re.sub('"','',link)
            return link
        except:
            return None
    except:
        return None


df_vacinas = get.get_noticias('G1')
ids_ainda_nao_coletados = get.get_dados_nao_inseridos('G1')

option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=r'./geckodriver', options=option)
for i in range(len(df_vacinas)):
    pk_id = df_vacinas['id'].iloc[i]
    if int(pk_id) in ids_ainda_nao_coletados:
        link = df_vacinas['link'].iloc[i]
        site = df_vacinas['site'].iloc[i]

        page = get_page(link)
        if page:
            scrapy_g1(page, pk_id, site)

driver.close()
 