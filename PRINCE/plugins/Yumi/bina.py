import requests
from PRINCE import app
from pyrogram import filters

# API Endpoint
API_URL = "https://ddg-api.herokuapp.com/search"

@app.on_message(filters.command("bingsearch"))
async def bing_search(bot, message):
    try:
        # Check if user provided a keyword
        if len(message.command) == 1:
            await message.reply_text("⚠️ Please provide a keyword to search.")
            return
        
        # Extracting search query from the command
        keyword = " ".join(message.command[1:])
        params = {"query": keyword}

        # Sending request to API
        response = requests.get(API_URL, params=params)
        
        # Checking API response
        if response.status_code == 200:
            results = response.json()
            if not results:
                await message.reply_text("❌ No results found.")
                return
            
            # Formatting results
            message_text = f"🔎 **Search Results for:** `{keyword}`\n\n"
            for result in results[:7]:  # Limiting to top 7 results
                title = result.get("title", "No Title")
                link = result.get("link", "#")
                message_text += f"🔹 [{title}]({link})\n"
            
            await message.reply_text(message_text, disable_web_page_preview=True)
        else:
            await message.reply_text("⚠️ API Error: Failed to fetch results.")
    
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
