import subprocess
import time
import threading
import requests
import pyautogui as pg
from decouple import config


BROWSER = config('BROWSER')
WHATSAPP_URL = config('WHATSAPP_URL')
TARGET_CONTACT = config('TARGET_CONTACT')
MESSAGE = config('MESSAGE')
NOTIFICATION_URL = config('NOTIFICATION_URL')
NOTIFICATION_BODY = {'sender': 'Whatsapp Bot', 'message': 'Mensagem enviada'}


def open_browser():
    global process
    process = subprocess.Popen([BROWSER, WHATSAPP_URL])


def select_chat():
    # Esperar o whatsapp web ser carregado
    while not pg.pixelMatchesColor(998, 379, (42, 148, 138)):
        print("aguardando...")
        time.sleep(1)
    print("carregado!")
    # Esperar a div de notificação aparecer
    time.sleep(10)
    # Localizar o ícone de busca
    search_icon_location = pg.locateCenterOnScreen('src/search_icon.png')
    # Clicar no ícone de busca
    pg.click(search_icon_location.x, search_icon_location.y)
    # Buscar o contato
    time.sleep(0.5)
    pg.write(TARGET_CONTACT)
    time.sleep(1)
    pg.click(x=291, y=348)
    time.sleep(1)
    pg.click(x=812, y=849)
    pg.write(MESSAGE)
    pg.press('enter')
    # dar um tempo para a mensagem ser enviada
    time.sleep(10)
    process.kill()
    # Enviar notificação para o Telegram avisando o sucesso
    print("Enviando notificação de sucesso")
    requests.post(NOTIFICATION_URL, json=NOTIFICATION_BODY)


process = None
thread_1 = threading.Thread(target=open_browser)
thread_2 = threading.Thread(target=select_chat)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("cabo")
