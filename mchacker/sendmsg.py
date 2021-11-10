import lotify
from lotify.client import Client

client = Client(
    client_id='RVtyKG2xWwJD8dpzg9qTNy',
    client_secret='7r6ylMKvIqLldcAgibPdOryOzOcSyhH6ou14bl9YDEX',
    redirect_uri='https://home.exodus.tw:5000/callback'
)
def msg(access_token,message):
    return client.send_message(access_token, message)
    #print(response)

i