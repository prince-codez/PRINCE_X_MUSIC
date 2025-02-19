from pyrogram import Client, filters
from faker import Faker
from PRINCE import app

fake = Faker()

@app.on_message(filters.command("fakeinfo"))
async def generate_info(client, message):
 
    name = fake.name()
    address = fake.address()
    country = fake.country()
    phone_number = fake.phone_number()
    email = fake.email()
    city = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()

    info_message = (
        f"ғᴜʟʟ ɴᴀᴍᴇ ➪  {name}\n"
        f"𝐀ᴅᴅʀᴇss ➪ {address}\n"
        f"𝐂ᴏᴜɴᴛʀʏ ➪ {country}\n"
        f"𝐏ʜᴏɴᴇ ɴᴜᴍʙᴇʀ ➪ {phone_number}\n"
        f"𝐄-ᴍᴀɪʟ ➪ {email}\n"
        f"𝐂ɪᴛʏ ➪ {city}\n"
        f"𝐒ᴛᴀᴛᴇ ➪ {state}\n"
        f"𝐙ɪᴘ ᴄᴏᴅᴇ ➪ {zipcode}"
    )

    await message.reply_text(info_message)  
