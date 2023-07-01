import requests, telebot
import threading, time
h = -1001863024342
def get():
    info =(requests.get("https://iraqborsa.uruk4apps.com/api/v3/summary.php").json())
    baghdad = info['b']
    south = info['s']
    north = info['n']
    return dict(buy=baghdad['buy'], sell=baghdad['sell'])


def background_task():
    # Code for your background task goes here
    while True:
        p = get()
        tohb = int(p['buy']) * 100
        tohs = int(p['sell']) * 100
        fo1 = "{:,}".format(tohb)
        fo2 = "{:,}".format(tohs)
        x = f"""
Buy <strong>{p['buy']}</strong> IQD
Sell <strong>{p['sell']}</strong> IQD

Buy:
  100$ USD => <strong>{fo1}</strong> IQD
Sell:
  100$ USD => <strong>{fo2}</strong> IQD
        """
        bot.send_message(chat_id=h, text=x, parse_mode="html")
        time.sleep(200)
bg_thread = threading.Thread(target=background_task)

# Start the thread
bg_thread.start()
bot = telebot.TeleBot("5923486919:AAFz0qpeJC1lCRRZGrmX3RVOMnoltrPMv84",parse_mode="markdown", num_threads=20, skip_pending=True)
try:
    bot.delete_webhook()
except:
    pass
@bot.message_handler(commands=['start'])
def start(message):
    p = get()
    tohb = int(p['buy']) * 100
    tohs = int(p['sell']) * 100
    fo1 = "{:,}".format(tohb)
    fo2 = "{:,}".format(tohs)
    x = f"""
Buy <strong>{p['buy']}</strong> IQD
Sell <strong>{p['sell']}</strong> IQD

Buy:
  100$ USD => <strong>{fo1}</strong> IQD
Sell:
  100$ USD => <strong>{fo2}</strong> IQD
    """
    bot.reply_to(message, x, parse_mode="html")

import os, json, requests, flask,time

import os, json, requests, flask,time

app = flask.Flask(__name__)

@app.route("/bot", methods=['POST'])
def getMessage():
  bot.process_new_updates([
    telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))
  ])
  return "!", 200


@app.route("/")
def webhook():
  bot.remove_webhook()
  link = 'https://'+str(flask.request.host)
  bot.set_webhook(url=f"{link}/bot")
  return "!", 200


app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
app = flask.Flask(__name__)
