import json
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from handlers.system import start, help, youtube_url, linkedIn_url, gmail_url, geeks_url
from handlers.chat import unknown, unknown_text

def main():
    with open("credentials.json", "r") as file:
        credentials = json.load(file)
    # Create Application instance
    bot_token = credentials["BOT_API_TOKEN"]
    application = Application.builder().token(bot_token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("youtube", youtube_url))
    application.add_handler(CommandHandler("linkedin", linkedIn_url))
    application.add_handler(CommandHandler("gmail", gmail_url))
    application.add_handler(CommandHandler("geeks", geeks_url))

    # Handle unknown text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_text))

    # Handle unknown commands
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Start the bot
    application.run_polling()


if __name__ == "__main__":
    main()
