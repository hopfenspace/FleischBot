import os, json
from telegram.ext import Updater, CommandHandler

with open ("Fleisch.json", "r+") as fd:
    Kontos=json.load(fd)

def Fleisch(bot,update):
    id=update.message.from_user.id
    id=str(id)
    update.message.reply_text("Und schon wieder ein totes Tier...")
    if id in Kontos:
        Kontos[id] = Kontos[id]+1
        with open ("Fleisch.json", "w") as fd:
            json.dump(Kontos,fd)
    else: 
        Kontos[id] = 1

def Fleischverbrauch(bot,update):
    id=str(update.message.from_user.id)
    if id in Kontos:
        update.message.reply_text(Kontos[id])
    else:
        Kontos[id] = 0
        with open ("Fleisch.json", "w") as fd:
            json.dump(Kontos,fd)
        update.message.reply_text(Kontos[id])
    

def Abschluss(bot,update):
    update.message.reply_text(Kontos)

def SetzeNull(bot,update):
    id=update.message.from_user.id
    id=str(id)
    Kontos[id] = 0
    with open ("Fleisch.json", "w") as fd:
            json.dump(Kontos,fd)

updater = Updater('860123473:AAFWU0FHzrcpOKCaS73KD5sTc67mQjX-EAg')
dp = updater.dispatcher
dp.add_handler(CommandHandler('Fleisch',Fleisch))
dp.add_handler(CommandHandler('Fleischverbrauch',Fleischverbrauch))
dp.add_handler(CommandHandler('Abschluss',Abschluss))
dp.add_handler(CommandHandler('SetzeNull', SetzeNull))
updater.start_polling()
updater.idle()
