# começando a mexer com selenium para web scrapping
import csv
import selenium
import time
from bs4 import BeautifulSoup
from selenium import webdriver

# # Definindo o caminho do webdriver que utilizarei
# PATH = "C:\Program Files (x86)\chromedriver_87.exe"

# # criando o driver e definindo que ele é do tipo do chrome.
# driver = webdriver.Chrome(PATH)

# definindo o site que ele realizará a busca

def monta_url(pesquisa):
    modelo = 'https://www.amazon.com.br/s?k={pesquisa}&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2'
    pesquisa = pesquisa.replace(' ', '+')

    # adicionando a url montada 
    url = modelo.format(pesquisa)
    
    # adicionando o numero de paginas
    url += '&page{}'

    return url

    # Extrai e retorna informações de um único registro
def extrator_dados(item):
    
    # descrição e url
    atag = item.h2.a
    descricao = atag.text.strip()
    url = 'https://amazon.com.br' + atag.get('href')
    try:
        # preço
        preco_pai = preco_pai.find('span', 'a-price')
        preco = preco_pai.find('span', 'a-offscreen').text
    except AtributeError:
        return

    try:
    # rankig e avaliações
        rating = item.i.text
        avaliacoes = item.find('span',{'class', 'a-size-base','dir','auto'}).text
    except AttributeError:
        rating = ''
        avaliacoes= ''

    resultado = (descricao, preco, rating,  avaliacoes, url )
    
    return resultado




def main(pesquisa):
    # Definindo o caminho do webdriver que utilizarei
    PATH = "C:\Program Files (x86)\chromedriver_87.exe"

    # criando o driver e definindo que ele é do tipo do chrome.
    driver = webdriver.Chrome(PATH)


    registros = []
    url = monta_url(pesquisa)
    
    for pagina in range(1,21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html-parser')
        registros = soup.find_all('div', {'data-componet-type':'s-search-result'})

        for item in registros:
            resultado = extrator_dados(item)
            if resultado:
                registro.append(registros)

    driver.close()

    with open('resultados.csv', 'w', newline = '', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow('Descrição', 'Preço', 'Rating', 'Avaliações', 'link')
        writer.writerows(registros)

if __name__ == "__main__":
    main('redragon')