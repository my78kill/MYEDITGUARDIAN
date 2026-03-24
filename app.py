from flask import Flask
import threading
import asyncio
import Aashik_Edit.main as bot

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is running 😈"

def run_bot():
    loop = asyncio.new_event_loop()   # 👈 create loop
    asyncio.set_event_loop(loop)      # 👈 set loop
    bot.app.run()                     # 👈 run pyrogram

# start bot thread
threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)
