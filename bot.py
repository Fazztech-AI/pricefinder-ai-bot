import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from engine import search_prices

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Pricefinder AI is online ✅\n\nTry: /price ps5"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    item = " ".join(context.args)

    if not item:
        await update.message.reply_text("Type something like: /price ps5")
        return

    await update.message.reply_text(f"Searching prices for: {item} 🔎")

    results = search_prices(item)

    if not results:
        await update.message.reply_text("No results found.")
        return

    message = ""
    for result in results[:3]:
        message += (
            f"Store: {result['store']}\n"
            f"Title: {result['title']}\n"
            f"Price: {result['price']}\n"
            f"Confidence: {result['confidence']}\n"
            f"Note: {result['note']}\n"
            f"Link: {result['url']}\n\n"
        )

    await update.message.reply_text(message[:3500])

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))

app.run_polling()
