import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Pricefinder AI is online ✅\n\nTry: /price strawberries"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    item = " ".join(context.args)

    if not item:
        await update.message.reply_text("Type something like: /price strawberries")
        return

    await update.message.reply_text(
        f"Searching prices for: {item}\n\nStore price search coming next 🔎"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))

app.run_polling()
