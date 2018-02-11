
import time
import sys
import telepot
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')

apitoken = cfg.get("Main", "token")
IDT = cfg.getint("Main", "id")
log = cfg.get("Main", "log")

bot = telepot.Bot(apitoken)
from telepot.loop import MessageLoop

def monitorar(path):
    with open(path, encoding="utf8") as arq:
        while True:
            nova_linha = arq.readline()
            nova_linha = nova_linha.replace('\n', '')
            if nova_linha:
                yield nova_linha
            else:
                time.sleep(1.0)

for idx, linha in enumerate(monitorar(log)):
    print("{:5d}: {}".format(idx, linha))
    if "Você are now job level" in linha:
        bot.sendMessage(IDT, linha)
    elif "Você está agora no nível" in linha:
        bot.sendMessage(IDT, linha)
    elif "Item Apareceu: Carta" in linha:
        bot.sendMessage(IDT, linha)
    elif "Por favor, selecione o seu destino." in linha:
        bot.sendMessage(IDT, "Teleportando via Kafra.")
    elif "NPC Funcionária Kafra (4): Digite" in linha:
        bot.sendMessage(IDT, "Bugado no armázen Kafra.")
