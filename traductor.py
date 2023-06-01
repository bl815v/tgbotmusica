import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from mtranslate import translate

# Configura el token de tu bot de Telegram
TOKEN = '5888238055:AAFzUBB71hcBRGr9nj84c5qPkg1IqO5HWQI'

# Configura el idioma de destino
target_language = 'es'  # Establece aquí el código del idioma al que deseas traducir (ejemplo: 'es' para español)

# Configura el registro de eventos
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Función para manejar el comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Soy un bot de traducción. ¡Envíame un mensaje y lo traduciré!")

# Función para manejar el comando /traducir
def traducir(update, context):
    text = update.message.reply_to_message.text
    translated_text = translate(text, target_language)
    context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)

# Función para manejar todos los mensajes de texto
def echo(update, context):
    text = update.message.text
    
    if text.startswith('/'):
        # Ignora los comandos
        return

    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def main():
    # Crea una instancia del bot
    bot = telegram.Bot(token=TOKEN)
    
    # Crea el objeto Updater y pasa la instancia del bot
    updater = Updater(bot=bot, use_context=True)

    # Obtiene el despachador para registrar manejadores
    dispatcher = updater.dispatcher

    # Agrega manejadores de comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("traducir", traducir))

    # Agrega un manejador para mensajes de texto
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

    # Inicia el bot
    updater.start_polling()

    # Ejecuta el bot hasta que se presione Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()