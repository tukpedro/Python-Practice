import pyautogui
import time
import pyperclip
import pandas as pd
from Tools.scripts.dutree import display

pyautogui.PAUSE = 1
pyautogui.alert('O script vai começar a rodar. Por favor, não mexa no PC enquanto não acabar')

# PASSO 1: ler o arquivo excel e calcular faturamento e quantidade de produtos

tabela = pd.read_excel(r'caminho do arquivo excel')
display(tabela)
faturamento = tabela['nome da coluna'].sum()
qtd_produtos = tabela['nome da coluna'].sum()
print(f'Total R${faturamento:.2f}\nQuantidade de Produtos: {qtd_produtos}')


# PASSO 2: abrir uma aba do navegador
pyautogui.hotkey('ctrl', 't')
link = 'link do seu email'

# copiar o link do seu email
pyperclip.copy(link)

# colar o link e entrar no seu email
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')

# esperar 3 segundos
time.sleep(3)

# PASSO 6: criar um novo email
pyautogui.click(x='posiçao do mouse eixo x', y='posiçao do mouse eixo y', clicks=1)
time.sleep(2)

# ecrever endereço do email destino
pyautogui.write('endereço de email destino')
pyautogui.press('tab')

# escrever assunto
pyautogui.press('tab')
assunto = 'Relatório de Vendas'
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')

# escrever no corpo do email
pyautogui.press('tab')
texto_email = f"""
Prezados,

O faturamento deste mês foi de: R${faturamento:,.2f}
A quantidade de produtos vendidos foi de: {qtd_produtos}

Abs,
(Seu nome)
"""
pyperclip.copy(texto_email)
pyautogui.hotkey('ctrl', 'v')

# PASSO 7: enviar o email para o destino
pyautogui.hotkey('ctrl', 'enter')
pyautogui.alert('Script finalizado')
