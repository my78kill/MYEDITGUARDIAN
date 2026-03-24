from flask import Flask
import threading
import Aashik_Edit.main as bot   # 👈 correct import

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running 😈"

def run_bot():
    bot.bot.infinity_polling()

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
