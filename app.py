from flask import Flask
import threading
import Aashik_Edit.main as bot

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is running 😈"

def run_bot():
    print("Bot starting...")
    bot.app.start()   # ❗ NO .run()
    print("Bot started")

# start bot in background
threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)
