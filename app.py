from flask import Flask
from Aashik_Edit.main import app as bot_app
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive 😈"

def run_bot():
    print("Bot starting...")
    bot_app.run()

# start bot in background
threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
