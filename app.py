from flask import Flask
import threading
import Aashik_Edit.main as bot   # 👈 correct import

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is running 😈"

# Pyrogram bot run function
def run_bot():
    bot.app.run()   # 👈 Pyrogram ke liye correct

# Start bot in background thread
threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # 👈 Render ke liye important
    app_flask.run(host="0.0.0.0", port=port)
