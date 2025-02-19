from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime, timedelta

# Pyrogram Client Initialize
app = Client("my_bot")

# Date to Day Command Handler
@app.on_message(filters.command("day"))
async def date_to_day_command(client: Client, message: Message):
    try:
        command_parts = message.text.split(" ", 2)
        
        if len(command_parts) == 1:
            await message.reply_text("⚠️ Usage: ➪ `/day YYYY-MM-DD`\n✅ Example: `/day 1947-08-15`")
            return
        
        input_date = command_parts[1].strip().replace("/", "-")  # Auto format correction

        if input_date.lower() == "today":
            date_object = datetime.today()
        else:
            try:
                date_object = datetime.strptime(input_date, "%Y-%m-%d")
            except ValueError:
                await message.reply_text("❌ Invalid format! 𝐔sᴇ `/day YYYY-MM-DD` (Example: `/day 1947-08-15`).")
                return
        
        # Check if extra argument is given
        if len(command_parts) == 3:
            option = command_parts[2].strip().lower()

            if option == "diff":  # Calculate Difference from Today
                today = datetime.today()
                diff_days = abs((today - date_object).days)
                await message.reply_text(f"📅 𝐃ᴀᴛᴇ ➪ {date_object.strftime('%Y-%m-%d')}\n🗓 𝐃ᴀʏ ➪ {date_object.strftime('%A')}\n⏳ ᴅᴀʏs 𝐃ɪғғᴇʀᴇɴᴄᴇ ➪ {diff_days} 𝐃ᴀʏs")
                return
            
            elif option == "next":  # Get Next Day
                date_object += timedelta(days=1)
            
            elif option == "prev":  # Get Previous Day
                date_object -= timedelta(days=1)

        # Final Output
        await message.reply_text(f"📅 𝐃ᴀᴛᴇ  ➪ {date_object.strftime('%Y-%m-%d')}\n🗓 𝐃ᴀʏ {date_object.strftime('%A')}")

    except Exception as e:
        await message.reply_text(f"🚨 Error: {str(e)}")

# Run the bot
app.run()
