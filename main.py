from pyrogram import Client, filters
from pyrogram.types import Message
import os

# Initialize the Pyrogram bot
api_id = 10738943
api_hash = 'da61e3a08b5ac78ce28b4a4cd854aeec'
bot_token = '6412441114:AAF5nri-Vw1kcwvMn4JT4KzXH2Fjpxv3HHA'

app = Client(
    "session_generator_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("Welcome! Send me /generate_session to generate a session string.")

@app.on_message(filters.command("generate_session"))
async def generate_session(_, message):
    # Generate a Pyrogram session string
    try:
        from pyrogram import Session
        session_name = message.from_user.username + ".session"
        session = Session(
            session_name,
            api_id=api_id,
            api_hash=api_hash,
        )
        session_string = await session.save()
        await message.reply(f"Your session string:\n```\n{session_string}\n```")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app.run()
