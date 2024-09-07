import time
from time import sleep as wait
from bale import Bot, Update, Message
keys = {"EHATS2-HSGA6-NSABAF", "ZoneLF", "TF625-78288-YUI9-2893", "UIOP8-98OPS-8909-KMNM", "89922-NAJAA-1111-0000", "OPOPO-POPOP-SENS-EGEN"}
time = {"سه روزه", "یک روزه", "سه ساعته", ""}
isValid = False

# Create an instance of the bot with your token
client = Bot(token="725904744:7WKxT4jOVXtz7C72FaDVGDDfsnPEccom9zmDaeh1")

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(client.user, "is Ready!")

# Event handler for handling messages
@client.event
async def on_message(message: Message):
    if message.content == "getid":
        await message.reply(text=f"{message.author.id}")
                
                

# Run the bot
client.run()
