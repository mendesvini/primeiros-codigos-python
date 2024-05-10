import pyautogui;
import time;
pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=955, y=599)

pyautogui.write('https://login.kroton.com.br/AccountAluno/Login?client_id=242337&response_type=code&state=b008e78df9adb596d7ccfb7f078549b5&referrer=portaldoaluno.faculdadepitagoras.com.br')
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=1485, y=470)
pyautogui.write('06586788331')
pyautogui.press('tab')
pyautogui.write('Mendesaraujo10')
pyautogui.press('tab')
pyautogui.press('enter')