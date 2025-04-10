from telegram.ext import Updater, CommandHandler

# Replace with your actual Telegram bot token
TOKEN = 'YOUR_BOT_TOKEN'

def start(update, context):
    update.message.reply_text("Hello! I'm alive on Koyeb!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
