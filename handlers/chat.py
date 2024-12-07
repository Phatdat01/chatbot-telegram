from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update
from telegram.ext import CallbackContext

# Handle unknown commands
async def unknown(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Sorry, '%s' is not a valid command" % update.message.text
    )


# Handle unknown text messages
async def unknown_text(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Sorry, I can't recognize you. You said '%s'" % update.message.text
    )