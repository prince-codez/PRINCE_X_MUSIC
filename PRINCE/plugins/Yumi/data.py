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
            date_object = datetime.today().date()  # Remove time part
        else:
            try:
                date_object = datetime.strptime(input_date, "%Y-%m-%d").date()
            except ValueError:
                await message.reply_text("❌ Invalid format! Use `/day YYYY-MM-DD` (Example: `/day 1947-08-15`).")
                return
        
        # Default response
        response_text = f"📅 𝐃ᴀᴛᴇ ➪ {date_object.strftime('%Y-%m-%d')}\n🗓 𝐃ᴀʏ ➪ {date_object.strftime('%A')}"

        # Check if extra argument is given
        if len(command_parts) == 3:
            option = command_parts[2].strip().lower()

            if option == "diff":  # Calculate Difference from Today
                today = datetime.today().date()
                diff_days = abs((today - date_object).days)
                response_text += f"\n⏳ 𝐃ᴀʏs 𝐃ɪғғᴇʀᴇɴᴄᴇ ➪ {diff_days} 𝐃ᴀʏs"
            
            elif option == "next":  # Get Next Day
                date_object += timedelta(days=1)
                response_text = f"📅 𝐍ᴇxᴛ 𝐃ᴀʏ ➪ {date_object.strftime('%Y-%m-%d')}\n🗓 𝐃ᴀʏ ➪ {date_object.strftime('%A')}"
            
            elif option == "prev":  # Get Previous Day
                date_object -= timedelta(days=1)
                response_text = f"📅 𝐏ʀᴇᴠɪᴏᴜs 𝐃ᴀʏ ➪ {date_object.strftime('%Y-%m-%d')}\n🗓 𝐃ᴀʏ ➪ {date_object.strftime('%A')}"
        
        # Send final response
        await message.reply_text(response_text)

    except Exception as e:
        await message.reply_text(f"🚨 Error: {str(e)}")

# Run the bot
app.run()
