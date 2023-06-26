from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = json.loads(request.data)
    event_type = request.headers.get('Twitch-Eventsub-Message-Type')

    if event_type == 'stream.online':
        channel_name = data['event']['broadcaster_user_name']
        print(f"{channel_name} is now live!")

    return 'OK'

if __name__ == '__main__':
    app.run()