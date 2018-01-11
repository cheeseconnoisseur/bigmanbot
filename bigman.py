from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    user = update.message.from_user
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")



def tube(bot, update):
    #update.message.reply_text("send vid name (n) or vid link(l)?")
    #bot.send_message(chat_id=update.message.chat_id, text="send vid name (n) or vid link(l)?")
    #chat_id = bot.get_updates()[-1].message.chat_id

    user = update.message.reply_text('send vid name (n) or vid link(l)?')
    update.message.reply_text(user)

def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    logger.info(user.first_name)
    update.message.reply_text('Maybe I can visit you sometime! '
                              'At last, tell me something about yourself.')

#def insert(bot, update):

#	user = update.message.from_user
#	text = update.message.text
#	caption = update.message.caption






def ugan(bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo='https://pbs.twimg.com/profile_images/948650214579044352/YAyu__6g_400x400.jpg')

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def main():
    updater = Updater(token='521816042:AAGUu7L6PEZIaFON3B96YHb-4MIqZouGME0')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("tube", tube))
    insert_handler = MessageHandler(Filters.location, location)
    dp.add_handler(CommandHandler("uganda", ugan))
    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(unknown_handler)
    #dp.add_handler(MessageHandler(Filters.text, echo))
    #dp.add_error_handler(error)
    updater.start_polling()

if __name__ == '__main__':
    main()
