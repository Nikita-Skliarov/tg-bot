import json
from include.json_parse import coins_data
from include.handlers import Start, Token_sale, Click_on_name_token, Token_sale_procedure, Handle_token_count, Submit_token_buy, Sale_status
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN_SALE_PROCEDURE, TOKEN_COUNT = range(2)

if __name__ == '__main__':
    application = ApplicationBuilder().token('7370415604:AAH21Q0Iv9FPdGD0eCZPhUqGt58PrmyRHDk').build()
    
    start_handler = CommandHandler('Start', Start)
    home_handler = CallbackQueryHandler(Start, pattern="home")
    token_sale_handler = CallbackQueryHandler(Token_sale, pattern="token_sale")
    
    # ConversationHandler for handling token sale process
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(Token_sale_procedure, pattern="sale")],
        states={
            TOKEN_SALE_PROCEDURE: [CallbackQueryHandler(Token_sale_procedure, pattern="sale")],
            TOKEN_COUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, Handle_token_count)]
        },
        fallbacks=[CommandHandler('start', Start)]
    )
    
    submit_token_buy_handler = CallbackQueryHandler(Submit_token_buy, pattern="set_queue")
    sale_status_handler = CallbackQueryHandler(Sale_status, pattern="sale_status")
    
    application.add_handler(home_handler)
    application.add_handler(start_handler)
    application.add_handler(token_sale_handler)
    application.add_handler(conv_handler)
    application.add_handler(submit_token_buy_handler)
    application.add_handler(sale_status_handler)
    
    for name in coins_data:
        handler = CallbackQueryHandler(
            lambda update, context, name=name: Click_on_name_token(update, context, name),
            pattern=name
        )
        application.add_handler(handler)  
    
    application.run_polling()