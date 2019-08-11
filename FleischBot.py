import os, json
from telegram.ext import Updater, CommandHandler

with open ("Fleisch.json", "r+") as fd:
    Kontos=json.load(fd)

def Fleisch(bot,update):
    id=update.message.from_user.id
    id=str(id)
    update.message.reply_text("Burn in hell")
    if id in Kontos:
        Kontos[id] = Kontos[id]+1
        with open ("Fleisch.json", "w") as fd:
            json.dump(Kontos,fd)
    else: 
        Kontos[id] = 1

def Fleischverbrauch(bot,update):
    id=str(update.message.from_user.id)
    update.message.reply_text(Kontos[id])



updater = Updater('youstupidshit')
dp = updater.dispatcher
dp.add_handler(CommandHandler('Fleisch',Fleisch))
dp.add_handler(CommandHandler('Fleischverbrauch',Fleischverbrauch))
updater.start_polling()
updater.idle()
