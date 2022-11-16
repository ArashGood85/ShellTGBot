# -*- coding: utf-8 -*-


from pyrogram import Client
from pyrogram.enums import ChatType
from subprocess import getoutput
from os import system, environ


ADMIN_USER_ID = environ.get("ADMIN_USER_ID")
BOT_API_TOKEN = environ.get("BOT_API_TOKEN")

if ADMIN_USER_ID != None or BOT_API_TOKEN != None:
    try:
        ADMIN_USER_ID = (int(ADMIN_USER_ID))
    except ValueError:
        print("\nError : ADMIN_USER_ID Is Not Integer .\n")
    else:
        print("Starting Bot ...\n")
        Bot = Client(
                      "Bot",
                      api_id=11960563,
                      api_hash="0d24b50792819b97546ff6168250d3ba",
                      bot_token=BOT_API_TOKEN
                    )

        @Bot.on_message()
        async def main(client, message):
            if (message.chat.type) == ChatType.PRIVATE:
                if (message.from_user.id) == ADMIN_USER_ID:
                    if (message.text) == "/start":
                        await Bot.send_message((message.chat.id), text="Bot Is Online ...")
                    elif ((message.text).startswith("/shell")) == True:
                        shell_command = (((message.text)[6:]).strip())
                        system(shell_command)
                        await Bot.send_message((message.chat.id), text="Executed ...")
                    elif ((message.text).startswith("/output")) == True:
                        shell_command = (((message.text)[7:]).strip())
                        shell_result = getoutput(shell_command)
                        await Bot.send_message((message.chat.id), text=(f"Result :\n\n{shell_result}"))
                    elif ((message.text).startswith("/pyexec")) == True:
                        py_code = (((message.text)[7:]).strip())
                        try:
                            exec(py_code)
                        except Exception as pyerror:
                            await Bot.send_message((message.chat.id), text=(f"Error :\n\n{pyerror}"))
                        else:
                            await Bot.send_message((message.chat.id), text="Executed ...")
        Bot.run()
else:
    print("\nError : ADMIN_USER_ID Or BOT_API_TOKEN Is NULL .\n")

