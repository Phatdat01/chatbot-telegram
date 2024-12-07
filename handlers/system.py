from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update
from telegram.ext import CallbackContext

# Start command handler
async def start(update: Update, context: CallbackContext):
    # Here, `update` represents the incoming message or command
    await update.message.reply_text(
        "Hello sir, Welcome to the Bot. Please write /help to see the commands available."
    )

# Help command handler
async def help(update: Update, context: CallbackContext):
    await update.message.reply_text(
        """Available Commands :- 
/youtube - To get the YouTube URL 
/linkedin - To get the LinkedIn profile URL 
/gmail - To get Gmail URL 
/geeks - To get the GeeksforGeeks URL"""
    )

# Command to provide Gmail URL
async def gmail_url(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Your Gmail link here (I am not giving mine for security reasons)"
    )

# Command to provide YouTube URL
async def youtube_url(update: Update, context: CallbackContext):
    await update.message.reply_text("YouTube Link => https://www.youtube.com/")


# Command to provide LinkedIn URL
async def linkedIn_url(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "LinkedIn URL => https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/"
    )

# Command to provide GeeksforGeeks URL
async def geeks_url(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "GeeksforGeeks URL => https://www.geeksforgeeks.org/"
    )