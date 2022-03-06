from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from  telegram import Update

def start(update=Update, context = CallbackContext):
    update.message.reply_text("Hi User")

def echo(update=Update, context = CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater("5146895402:AAFef00fvBuAXzHLUkHhLMEfcIqOEGD4qdc")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


main()
print('поставьте 3 кристалика пж пж пж пж')