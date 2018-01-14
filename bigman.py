from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import logging
import telegram
from pytube import YouTube
from calendarrr import maincal
import os
import random


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

BIO, HM = range(2)

def start(bot, update):
    user = update.message.from_user
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")



def tube(bot, update):
    #update.message.reply_text("send vid name (n) or vid link(l)?")
    #bot.send_message(chat_id=update.message.chat_id, text="send vid name (n) or vid link(l)?")
    #chat_id = bot.get_updates()[-1].message.chat_id
    update.message.reply_text('send link')

    return BIO

def location(bot, update):
    user = update.message.text
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING, timeout = 600)
    logger.info("starting")
    #update.message.reply_text(update.message.text)
    print(user)
    yt = YouTube(update.message.text)
    #yt = YouTube("https://www.youtube.com/watch?v=)
    title = yt.title
    stream = yt.streams.first()
    bot.send_message(chat_id=update.message.chat_id,message_id=123, text="downlaoding")
    stream.download()
    oldtitle = title
    bot.send_message(chat_id=update.message.chat_id,message_id=123, text="uploading")
    #title = title.replace(".","")
    #title = title + ".mp4"
    #title = title.replace(":","")
    #title = title.replace(",","")
    #title = title.replace("?","")
    #print(title)
    ##YouTube(update.message.text).streams.first().download('media')
    #bot.send_document(chat_id=update.message.chat_id, document=open(title, 'rb'),timeout=600)

    try:
        title = title.replace(".","")
        title = title + ".mp4"
        title = title.replace(":","")
        title = title.replace(",","")
        title = title.replace("?","")
        #YouTube(update.message.text).streams.first().download('media')
        bot.send_document(chat_id=update.message.chat_id, document=open(title, 'rb'),timeout=600)
    except:
        print("lolno")
    try:
        oldtitle = oldtitle + ".webm"
        oldtitle = oldtitle.replace(":","")
        oldtitle = oldtitle.replace("?","")
        #YouTube(update.message.text).streams.first().download('media')
        bot.send_document(chat_id=update.message.chat_id, document=open(oldtitle, 'rb'),timeout=600)

    except:
        print("lolno")
    try:
        os.remove(title)
    except:
        print("no1")
    try:
        os.remove(oldtitle)
    except:
        print("no2")

    print("lol")
    return (update.message.text)
    #add a thing that looks for https things here

#def insert(bot, update):

#	user = update.message.from_user
#	text = update.message.text
#	caption = update.message.caption

def cal(bot, update):
    update.message.reply_text('how many events?')
    return HM

def calget(bot, update):
    user = update.message.text
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING, timeout = 600)
    logger.info("starting")
    maincal(int(user))
    kay = []
    with open('temp.txt','r') as f:
        kay = f.read()
        kay = kay.split("\n")
        print(kay)
    for event in kay:
        print(kay)
        event = str(event)
        bot.send_message(chat_id=update.message.chat_id,message_id=123, text= event)


def calnext(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING, timeout = 600)
    logger.info("starting")
    maincal(1)
    kay = []
    with open('temp.txt','r') as f:
        kay = f.read()
        kay = kay.split("\n")
        print(kay)
    for event in kay:
        print(kay)
        event = str(event)
        bot.send_message(chat_id=update.message.chat_id,message_id=123, text= event)


def ugan(bot, update):
    bigint = random.randint(1,16)
    if bigint == 1:
        bot.send_photo(chat_id=update.message.chat_id, photo='https://pbs.twimg.com/profile_images/948650214579044352/YAyu__6g_400x400.jpg')
    elif bigint == 2:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/328/838/c81.png')
    elif bigint == 3:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/328/900/8e4.jpg')
    elif bigint == 4:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/331/654/bb9.png')
    elif bigint == 5:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/330/540/7c2.jpg')
    elif bigint == 6:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/330/213/450.png')
    elif bigint == 7:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/329/423/500.jpg')
    elif bigint == 8:
        bot.send_photo(chat_id=update.message.chat_id, photo='https://pics.me.me/ugandan-knuckles-30-hp-basic-this-is-not-the-way-30196890.png')
    elif bigint == 9:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/329/356/a9c.jpg')
    elif bigint == 10:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/331/504/bd8.png')
    elif bigint == 11:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/331/353/919.jpg')
    elif bigint == 12:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/328/898/e9f.jpg')
    elif bigint == 13:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/331/321/c62.png')
    elif bigint == 14:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/331/220/c8e.jpg')
    elif bigint == 15:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/330/487/295.jpg')
    elif bigint == 16:
        bot.send_photo(chat_id=update.message.chat_id, photo='http://i0.kym-cdn.com/photos/images/newsfeed/001/330/260/2f3.jpg')

def logan(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo='http://glamourlifestyles.com/wp-content/uploads/2018/01/logan-paul.jpg')

def tide(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo='https://i.redd.it/7po4xlcy6j701.jpg')
    bot.send_photo(chat_id=update.message.chat_id, photo='https://twitter.com/Tidepodmemes/status/949693054054670336/photo/1')

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def main():
    updater = Updater(token='521816042:AAGUu7L6PEZIaFON3B96YHb-4MIqZouGME0')
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("tube", tube)],

        states={

            BIO: [MessageHandler(Filters.text, location)]
        },

        fallbacks=[CommandHandler("uganda", ugan)]
    )

    conv_handler2 = ConversationHandler(
        entry_points=[CommandHandler("cal", cal)],

        states={

            HM: [MessageHandler(Filters.text, calget)]
        },

        fallbacks=[CommandHandler("uganda", ugan)]
    )
    dp.add_handler(conv_handler)
    dp.add_handler(conv_handler2)
    dp.add_handler(CommandHandler("start", start))
    #dp.add_handler(MessageHandler(Filters.text, location))
    dp.add_handler(CommandHandler("uganda", ugan))
    #dp.add_handler(CommandHandler("cal", cal))
    dp.add_handler(CommandHandler("calnext", calnext))
    dp.add_handler(CommandHandler("logan", logan))
    dp.add_handler(CommandHandler("tide", tide))
    unknown_handler = MessageHandler(Filters.command, unknown, pass_chat_data=True)
    dp.add_handler(unknown_handler)
    #dp.add_handler(MessageHandler(Filters.text, echo))
    #dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
