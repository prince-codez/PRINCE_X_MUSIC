from PRINCE import app
import requests as r
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters

API_URL = "https://sugoi-api.vercel.app/search"

@app.on_message(filters.command("bingsearch"))
async def bing_search(client, message):
    try:
        if len(message.command) == 1:
            await message.reply_text("🔍 **Please provide a keyword to search.**\n\nExample: `/bingsearch python tutorial`")
            return

        keyword = " ".join(message.command[1:])
        params = {"keyword": keyword}
        response = r.get(API_URL, params=params)

        if response.status_code == 200:
            results = response.json()
            if not results:
                await message.reply_text("❌ **No results found.** Try another keyword.")
            else:
                buttons = []
                for result in results[:5]:  # Top 5 results
                    title = result.get("title", "Unknown Title")
                    link = result.get("link", "#")
                    buttons.append([InlineKeyboardButton(text=title, url=link)])

                await message.reply_text(
                    f"🔎 **Search Results for:** `{keyword}`",
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
        else:
            await message.reply_text("⚠️ **API Error: Failed to fetch results.**")
    except Exception as e:
        await message.reply_text(f"🚨 **An error occurred:** `{str(e)}`")
