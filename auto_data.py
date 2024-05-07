import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(3)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)
pyautogui.click(x=743, y=513)
pyautogui.write('test_system_7@outlook.com')
pyautogui.press('tab')
pyautogui.write('777777')
pyautogui.press('enter')

time.sleep(3)

import pandas as pd

tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    #cod produto
    pyautogui.click(x=653, y=367)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))

    #marca
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))

    #tipo
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))

    #categoria
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))

    #preço un.
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))

    #custo
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))

    #observação
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'obs']))
    
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)