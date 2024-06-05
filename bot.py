# commands.py has all replies to / commands
from handlers import Start, Continue

# telegram bot library
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    application = ApplicationBuilder().token('7370415604:AAH21Q0Iv9FPdGD0eCZPhUqGt58PrmyRHDk').build()
    
    start_handler = CommandHandler('Start', Start)
    continue_handler = CallbackQueryHandler(Continue, pattern="continue")
    application.add_handler(start_handler)
    application.add_handler(continue_handler)
    application.run_polling()