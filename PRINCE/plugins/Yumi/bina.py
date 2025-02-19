import requests
from PRINCE import app
from pyrogram import filters

# ✅ Official DuckDuckGo API
API_URL = "https://api.duckduckgo.com/"

@app.on_message(filters.command("bingsearch"))
async def bing_search(bot, message):
    try:
        # Check if user provided a keyword
        if len(message.command) == 1:
            await message.reply_text("⚠️ Please provide a keyword to search.")
            return
        
        # Extract search query
        keyword = " ".join(message.command[1:])
        params = {"q": keyword, "format": "json"}

        # API Request
        response = requests.get(API_URL, params=params)

        # Check if API responded successfully
        if response.status_code == 200:
            data = response.json()
            results = data.get("RelatedTopics", [])

            if not results:
                await message.reply_text("❌ No results found.")
                return

            # Formatting results
            message_text = f"🔎 **Search Results for:** `{keyword}`\n\n"
            count = 0
            for result in results:
                if "Text" in result and "FirstURL" in result:
                    title = result["Text"]
                    link = result["FirstURL"]
                    message_text += f"🔹 [{title}]({link})\n"
                    count += 1
                    if count == 7:  # Limit to 7 results
                        break
            
            await message.reply_text(message_text, disable_web_page_preview=True)
        else:
            await message.reply_text("⚠️ API Error: Failed to fetch results.")
    
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
