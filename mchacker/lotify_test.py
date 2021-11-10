import lotify
from lotify.client import Client
import json
from flask import Flask, render_template
from flask import request
import urllib
import pymysql
import db

app = Flask(__name__)

client = Client(
    client_id='RVtyKG2xWwJD8dpzg9qTNy',
    client_secret='7r6ylMKvIqLldcAgibPdOryOzOcSyhH6ou14bl9YDEX',
    redirect_uri='https://home.exodus.tw:5000/callback'
)

user_id = ""
link = client.get_auth_link(state='*')
print(link)


@app.route("/callback")
def callback_nofity():
    assert request.headers['referer'] == 'https://notify-bot.line.me/'
    code = request.args.get('code')
    state = request.args.get('state')

    print(code)

    access_token = get_token(code, client.client_id, client.client_secret, client.redirect_uri)

    # send_message(access_token,"\n \n   給你看看這隻可愛的柴犬    \n\n","https://i.imgur.com/WH6QIAs.jpeg")

    # response = client.send_message(access_token, message='This is notify message')
    # print(response)
    db.db_add(user_id,access_token)
    return render_template('index.html')
    # return '恭喜完成 LINE Notify 連動！請關閉此視窗。'

def get_token(code, client_id=client.client_id, client_secret=client.client_secret, redirect_uri=client.redirect_uri):
    url = 'https://notify-bot.line.me/oauth/token'
    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers)
    page = urllib.request.urlopen(req).read()

    res = json.loads(page.decode('utf-8'))
    print(res)
    return res['access_token']

def send_message(access_token, text_message, picurl):

    url = 'https://notify-api.line.me/api/notify'
    headers = {"Authorization": "Bearer "+ access_token}

    data = {'message': text_message,
            'imageThumbnail':picurl, 'imageFullsize':picurl
            }

    data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers)
    page = urllib.request.urlopen(req).read()

@app.route("/notify")
def home():
    user_id = request.args.get('id')
    return render_template('home.html',url=link)

if __name__ == "__main__":
    #app.run(debug=True)
	app.run(host='0.0.0.0',debug=True,ssl_context=('/etc/letsencrypt/live/home.exodus.tw/fullchain.pem', '/etc/letsencrypt/live/home.exodus.tw/privkey.pem'))

# var privateKey  = fs.readFileSync('/etc/letsencrypt/live/home.exodus.tw/privkey.pem')
#  var certificate = fs.readFileSync('/etc/letsencrypt/live/home.exodus.tw/fullchain.pem')

# link = client.get_auth_link(state='RANDOM_STRING')
# print(link)
#
# access_token = client.get_access_token(code='NOTIFY_RESPONSE_CODE')
# print(access_token)
#
# status = client.status(access_token='YOUR_ACCESS_TOKEN')
# print(status)
#
# response = client.send_message(access_token='YOUR_ACCESS_TOKEN', message='This is notify message')
# print(response)


# curl -d "grant_type=authorization_code&redirect_uri=https://e5bb-2001-288-4001-d833-df5-4aa8-51a-528b.ngrok.io&client_id=RVtyKG2xWwJD8dpzg9qTNy&client_secret=7r6ylMKvIqLldcAgibPdOryOzOcSyhH6ou14bl9YDEX&code=bH5Y8FEC0WTuxuyYKiG5bG" https://notify-bot.line.me/oauth/token

 # curl -Uri 'https://notify-bot.line.me/oauth/token' -Body "grant_type=authorization_code&redirect_uri=https://e5bb-2001-288-4001-d833-df5-4aa8-51a-528b.ngrok.io&client_id=RVtyKG2xWwJD8dpzg9qTNy&client_secret=7r6ylMKvIqLldcAgibPdOryOzOcSyhH6ou14bl9YDEX
