import os, urllib

client_id = os.environ['NOTIFY_CLIENT_ID']
client_secret = os.environ['NOTIFY_CLIENT_SECRET']
redirect_uri = f"https://{os.environ['YOUR_HEROKU_APP_NAME']}.herokuapp.com/callback/notify"

def create_auth_link(user_id, client_id=client_id, redirect_uri=redirect_uri):
    
    data = {
        'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'scope': 'notify',
        'state': user_id
    }
    query_str = urllib.parse.urlencode(data)

    return f'https://notify-bot.line.me/oauth/authorize?{query_str}'
