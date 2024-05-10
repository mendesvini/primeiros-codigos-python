import pyautogui
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=950, y=613)
time.sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=1147, y=470)
pyautogui.write('mendesaraujovinicius87@gmail.com')
pyautogui.press('tab')
pyautogui.write('araujo10*')
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)


import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)


for linha in tabela.index:
    codigo = str(tabela.loc[linha,'codigo'])
    pyautogui.click(x=879, y=318)
    pyautogui.write(codigo)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'custo']))
    pyautogui.press('tab')
    obs = str(tabela.loc[linha,'obs'])
    if obs != 'nan':
       pyautogui.write(obs)
    pyautogui.press('tab') 
    pyautogui.press('enter')
    pyautogui.scroll(5000) 


