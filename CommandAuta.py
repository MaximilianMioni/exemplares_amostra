import pyautogui
import time

print('COMMANDAUTA')
print('Programa de Automação de comandos PROMPT para limpeza e reparo do Windows')
print(' ')
print('Ao continuar, o PROMPT de comando será executado')
print('Arquivos temporários serão excluídos do seu computador')
print(' ')
print('Tecle "ENTER" para iniciar/repetir o processo ou "S" para encerrar o programa.')

while True:

    comando = input('')

    if comando == '': 

        pyautogui.PAUSE = 1

        pyautogui.press('win')
        pyautogui.write('prompt de comando')

        time.sleep(2)
        pyautogui.press('enter')

        time.sleep(2)
        pyautogui.write('del /q/f/s %TEMP%\ ')
        pyautogui.press('enter')

        time.sleep(3)
        pyautogui.hotkey('alt', 'f4')

    elif comando == 's' or 'S':
        break