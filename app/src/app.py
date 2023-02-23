from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def today_datetime():
    now = datetime.datetime.now()
    #today = datetime.date.today()
    now = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    return f"Hello, 現在の日時は {now}です。 How are you?"

@app.route('/app')
def hoge_world():
    return 'Hello!! App'

if __name__ == '__main__':
    app.run(debug=True)