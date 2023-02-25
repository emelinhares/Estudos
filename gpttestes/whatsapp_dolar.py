from selenium import webdriver
import requests
import time
import os

# define o caminho para o Chrome WebDriver
driver_path = os.path.join(os.getcwd(), 'chromedriver.exe')


# Abre o Google Chrome
driver = webdriver.Chrome()

# Abre o WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Espera o usuário fazer o login no WhatsApp Web
input('Faça o login no WhatsApp Web e pressione enter para continuar')

# Obtém o valor do dólar através da API do Banco Central
response = requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json')
dolar = response.json()[0]['valor']

# Formata a mensagem a ser enviada
mensagem = f'O valor atual do dólar é R$ {dolar:.2f}'

# Busca pelo contato 'Drikão'
contato = driver.find_element_by_xpath('//span[@title="Drikão"]')

# Clica no contato
contato.click()

# Espera um segundo para carregar a conversa
time.sleep(1)

# Busca pelo campo de mensagem
mensagem_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')

# Digita a mensagem
mensagem_box.send_keys(mensagem)

# Aperta a tecla Enter para enviar a mensagem
mensagem_box.send_keys('\n')

# Espera 3 segundos para a mensagem ser enviada
time.sleep(3)

# Fecha o navegador
driver.quit()
