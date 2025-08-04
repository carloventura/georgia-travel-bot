import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from data import ITINERARIO, RISTORANTI, BIGLIETTI

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Ottieni il token del bot da una variabile d'ambiente
TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start per dare il benvenuto e spiegare i comandi disponibili"""
    await update.message.reply_text(
        "👋 Benvenuto nel tuo Bot per il viaggio in Georgia!\n\n"
        "Comandi disponibili:\n"
        "/itinerario - Mostra le tappe del viaggio\n"
        "/ristoranti - Mostra i ristoranti salvati\n"
        "/biglietti - Mostra i codici dei biglietti\n"
    )

async def itinerario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /itinerario per mostrare le tappe del viaggio"""
    message = "📍 *ITINERARIO DEL VIAGGIO*\n\n"
    for tappa in ITINERARIO:
        message += f"*{tappa['tappa']} - {tappa['giorni']}*\n"
        message += f"📝 {tappa['descrizione']}\n"
        message += f"🏨 Hotel: {tappa['hotel']}\n\n"
    await update.message.reply_text(message, parse_mode='Markdown')

async def ristoranti(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /ristoranti per mostrare i ristoranti salvati"""
    message = "🍽 *RISTORANTI*\n\n"
    for ristorante in RISTORANTI:
        message += f"*{ristorante['nome']}* - {ristorante['città']}\n"
        message += f"Cucina: {ristorante['tipo']}\n"
        message += f"📍 {ristorante['indirizzo']}\n"
        message += f"📝 {ristorante['note']}\n\n"
    await update.message.reply_text(message, parse_mode='Markdown')

async def biglietti(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /biglietti per mostrare i codici dei biglietti"""
    message = "🎫 *BIGLIETTI*\n\n"
    for biglietto in BIGLIETTI:
        message += f"*{biglietto['tipo']}*\n"
        message += f"📅 Data: {biglietto['data']}\n"
        message += f"✈️ {biglietto['dettagli']}\n"
        message += f"🎟 Codice: `{biglietto['codice']}`\n\n"
    await update.message.reply_text(message, parse_mode='Markdown')

def main():
    """Funzione principale per avviare il bot"""
    # Crea l'applicazione
    application = Application.builder().token(TOKEN).build()

    # Aggiungi i command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("itinerario", itinerario))
    application.add_handler(CommandHandler("ristoranti", ristoranti))
    application.add_handler(CommandHandler("biglietti", biglietti))

    # Avvia il bot
    print("Bot avviato!")
    application.run_polling()

if __name__ == '__main__':
    main()
