from flask import Flask, request
import requests
import json
import traceback
import random
app = Flask(__name__)
token = ""
@app.route('/', methods=['GET', 'POST'])
def home():
  return 'Incio del server del servidor'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
  if request.method == 'POST':
    output = request.get_json()

    print(str("---"))
    print(str(output))
    print(str("---"))
  
    for event in output['entry']:
      messaging = event['messaging']
      for eventMessage in messaging:
        recipient_id = eventMessage['sender']['id']
        payload = {'recipient': {'id': recipient_id}, 'message': {'text': "Hello World"}}
        r = requests.post('https://graph.facebook.com/v2.6/me/messages/?access_token=' + token, json=payload)
        
    return "ok"
  elif request.method == 'GET': # For the initial verification
    if request.args.get('hub.verify_token') == 'MyToken':
      return request.args.get('hub.challenge')
    return "Wrong Verify Token"


if __name__ == '__main__':
  app.run(debug=True)
