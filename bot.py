import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configurazione logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Definisci le opzioni del menu
menu_options = [['Ritaglia GIF'], ['Converti GIF in Emoji Animata'], ['Esci']]

# Funzione start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(menu_options, one_time_keyboard=True)
    await update.message.reply_text('Ciao! Scegli cosa vuoi fare:', reply_markup=reply_markup)

# Funzione per gestire le opzioni del menu
async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == 'Ritaglia GIF':
        await update.message.reply_text('Inviami la GIF da ritagliare.')
    elif text == 'Converti GIF in Emoji Animata':
        await update.message.reply_text('Inviami la GIF da convertire in emoji animata.')
    elif text == 'Esci':
        await update.message.reply_text('Bot terminato. A presto!')
    else:
        await update.message.reply_text('Opzione non valida. Usa il menu per scegliere un\'opzione.')

# Funzione per gestire le GIF
async def handle_gif(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    await file.download_to_drive('input.gif')
    
    text = context.user_data.get('last_option')
    if text == 'Ritaglia GIF':
        # Implementa la logica per ritagliare la GIF
        await update.message.reply_text('GIF ritagliata e salvata come "output.gif".')
    elif text == 'Converti GIF in Emoji Animata':
        # Implementa la logica per convertire la GIF in emoji animata
        await update.message.reply_text('GIF convertita in emoji animata e salvata come "output.gif".')
    else:
        await update.message.reply_text('Errore: Nessuna opzione valida selezionata.')

# Funzione principale per avviare il bot
def main():
    application = Application.builder().token("7430248929:AAEFv-FIC40br_nz1gylJ9lZ0YNzEYKuLio").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))
    application.add_handler(MessageHandler(filters.Document.MIME_type("image/gif"), handle_gif))

    application.run_polling()

if __name__ == '__main__':
    main()

