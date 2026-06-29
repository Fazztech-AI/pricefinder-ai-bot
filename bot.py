import os
from dotenv import load_dotenv

load_dotenv()
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

    message = f"Best prices for: {item}\n\n"

    for index, result in enumerate(results[:5], start=1):
        message += (
            f"{index}. {result['store']}\n"
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

if __name__ == "__main__":
    app.run_polling()