import os, json
from telegram.ext import Updater, CommandHandler

with open ("Fleisch.json", "r+") as fd:
    Kontos=json.load(fd)

FleischMessages = [
	"Und schon wieder ein totes Tier...",
	"Der Meeresspiegel steigt! 🌊",
	"Iss auch mal einen Salat!",
	"🐷 REDRUM",
	"10 years from now... - Remember how we used to have snow in the winter? 😔",
    "20 years from now... - Remember how we were able to drink water from the sink? 💧",
    "50 years from now... - grandpa/ma, what's a snowman? ☃️",
    "100 years fro-; OH, never mind, you died :-) 🌄"
]

def Fleisch(bot,update):
    id=update.message.from_user.id
    id=str(id)
    update.message.reply_text(random.choice(FleischMessages)
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

updater = Updater('Add your token')
dp = updater.dispatcher
dp.add_handler(CommandHandler('Fleisch',Fleisch))
dp.add_handler(CommandHandler('Fleischverbrauch',Fleischverbrauch))
dp.add_handler(CommandHandler('Abschluss',Abschluss))
dp.add_handler(CommandHandler('SetzeNull', SetzeNull))
updater.start_polling()
updater.idle()
