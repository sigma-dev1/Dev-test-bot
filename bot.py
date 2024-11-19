import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup

# Configurazione logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Definisci le opzioni del menu
menu_options = [['Ritaglia GIF'], ['Converti GIF in Emoji Animata'], ['Esci']]

# Funzione start
def start(update, context):
    reply_markup = ReplyKeyboardMarkup(menu_options, one_time_keyboard=True)
    update.message.reply_text('Ciao! Scegli cosa vuoi fare:', reply_markup=reply_markup)

# Funzione per gestire le opzioni del menu
def handle_menu(update, context):
    text = update.message.text
    
    if text == 'Ritaglia GIF':
        update.message.reply_text('Inviami la GIF da ritagliare.')
    elif text == 'Converti GIF in Emoji Animata':
        update.message.reply_text('Inviami la GIF da convertire in emoji animata.')
    elif text == 'Esci':
        update.message.reply_text('Bot terminato. A presto!')
    else:
        update.message.reply_text('Opzione non valida. Usa il menu per scegliere un\'opzione.')

# Funzione per gestire le GIF
def handle_gif(update, context):
    file = update.message.document.get_file()
    file.download('input.gif')
    
    text = context.user_data.get('last_option')
    if text == 'Ritaglia GIF':
        # Implementa la logica per ritagliare la GIF
        update.message.reply_text('GIF ritagliata e salvata come "output.gif".')
    elif text == 'Converti GIF in Emoji Animata':
        # Implementa la logica per convertire la GIF in emoji animata
        update.message.reply_text('GIF convertita in emoji animata e salvata come "output.gif".')
    else:
        update.message.reply_text('Errore: Nessuna opzione valida selezionata.')

# Funzione principale per avviare il bot
def main():
    updater = Updater("7430248929:AAEFv-FIC40br_nz1gylJ9lZ0YNzEYKuLio")  # Rimuovi 'use_context=True'
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))
    dp.add_handler(MessageHandler(filters.Document.MIME_type("image/gif"), handle_gif))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
