from datetime import datetime
import pyautogui as pa
import time
import random

cont = 0
loop = random.randrange(15, 30)

dt_inicio_pro = datetime.now()

while cont < loop:
    dt_inicio = datetime.now()
    aleat = random.randrange(120, 260)
    cont += 1
    print(f'Inicio: {dt_inicio}\nContagem: {cont}/{loop}\nSegundos: {aleat} seg\nMinutos: {aleat/60:.0f} min\n')
    time.sleep(aleat)
    if_aleat = random.randint(1, 3)
    if if_aleat == 1:
        pa.hotkey('alt', 'tab')
        time.sleep(3)
        pa.hotkey('alt', 'tab')
        print('Comando: Alt + Tab')
    elif if_aleat == 2:
        pa.press('win')
        time.sleep(3)
        pa.press('win')
        print('Comando: Win')
    elif if_aleat == 3:
        pa.hotkey('win', 'd')
        time.sleep(3)
        pa.hotkey('win', 'd')
        print('Comando: Win + D')
    else:
        pa.hotkey('win', 'tab')
        time.sleep(3)
        pa.hotkey('win', 'tab')
        print('ELSE: Win + Tab')
    dt_fim = datetime.now()
    print(f'Fim: {dt_fim}\n', '=*='*8)
dt_fim_pro = datetime.now()
print(f'\nInicio Programa{dt_inicio_pro}')
print(f'\nFim Programa{dt_fim_pro}')
print(f'Duração: {dt_fim_pro - dt_inicio_pro}')