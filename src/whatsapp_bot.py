import subprocess
import time
import threading
import pyautogui as pg


BROWSER = 'firefox'
WHATSAPP_URL = 'https://web.whatsapp.com/'
TARGET_CONTACT = 'x-defi'
MESSAGE = 'teste'


def open_browser():
    global process
    process = subprocess.Popen([BROWSER, WHATSAPP_URL])


def select_chat():
    while not pg.pixelMatchesColor(1005, 403, (26, 132, 120)):
        print("aguardando...")
        time.sleep(1)
    print("carregado!")
    time.sleep(10)
    pg.click(x=223, y=305)
    pg.write(TARGET_CONTACT)
    time.sleep(1)
    pg.click(x=291, y=348)
    time.sleep(1)
    pg.click(x=812, y=849)
    pg.write(MESSAGE)
    pg.press('enter')
    process.kill()


process = None
thread_1 = threading.Thread(target=open_browser)
thread_2 = threading.Thread(target=select_chat)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("cabo")
