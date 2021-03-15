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



folha_sp_login = 'https://login.folha.com.br/login?service=paywall%2Ffrontend&done=https%3A%2F%2Fwww.folha.uol.com.br%2F'
email = 'xx'
password = 'xx' 

option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=r'./geckodriver', options=option)

#login
driver.get(folha_sp_login)

email_element = driver.find_element_by_xpath('//*[@id="registerEmail"]')
password_element = driver.find_element_by_xpath('//*[@id="registerPassword"]')
button_login = driver.find_element_by_xpath('/html/body/main/section/div[2]/div/div[1]/div/div/form/div[4]/button')

email_element.send_keys(email)
password_element.send_keys(password)
driver.execute_script('arguments[0].click();', button_login)


df_vacinas = get.get_noticias('Folha')
ids_ainda_nao_coletados = get.get_dados_nao_inseridos('Folha')

#busca noticia
for i in range(len(df_vacinas)):
    pk_id = df_vacinas['id'].iloc[i]
    if int(pk_id) in ids_ainda_nao_coletados:
        noticia = df_vacinas['link'].iloc[i]
        sleep(2)
        driver.get(noticia)
        sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(4)
        try:
            button_comentarios = driver.find_element_by_css_selector('.more')
            driver.execute_script('arguments[0].click();', button_comentarios)
            sleep(5)
       
            main = driver.find_elements_by_class_name('main')
            html = main[0].get_attribute('innerHTML')

            soup = BeautifulSoup(html, 'html.parser')   
            comentarios = soup.find_all('p', attrs = {'class':'c-list-comments__comment'})

            for comentario in comentarios:
                insert_in_bd(comentario.text, pk_id, 'Folha')
        except:
            continue

        print('---- ** ---')

driver.close()
