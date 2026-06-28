import os
import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def search_jbhifi(item):
    search_url = f"https://www.jbhifi.com.au/search?page=1&query={item.replace(' ', '%20')}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(search_url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(" ", strip=True)

    return {
        "store": "JB Hi-Fi",
        "search_url": search_url,
        "preview": text[:500]
    }

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Pricefinder AI is online ✅\n\nTry: /price ps5"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    item = " ".join(context.args)

    if not item:
        await update.message.reply_text("Type something like: /price ps5")
        return

    await update.message.reply_text(f"Searching JB Hi-Fi for: {item} 🔎")

    try:
        result = search_jbhifi(item)

        await update.message.reply_text(
            f"Store checked: {result['store']}\n\n"
            f"Search link:\n{result['search_url']}\n\n"
            f"Page preview:\n{result['preview']}"
        )

    except Exception as e:
        await update.message.reply_text(f"Search failed: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))

app.run_polling()
