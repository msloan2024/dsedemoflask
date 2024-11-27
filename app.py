from flask import Flask, render_template, jsonify, Response
import houndify
import base64
import os

app = Flask(__name__)

# Houndify credentials
CLIENT_ID = os.getenv("CLIENT_ID", default="password")
CLIENT_KEY = os.getenv("CLIENT_KEY", default="password")

userId = "dsedemoflask"
requestInfo = {
    'Latitude': 37.388309,
    'Longitude': -121.973968,
    'ResponseAudioVoice' : 'Echo',
    'ResponseAudioShortOrLong' : 'Short',
    'ResponseAudioEncoding' : 'WAV'
}

# Initialize Houndify client
client = houndify.TextHoundClient(CLIENT_ID, CLIENT_KEY, userId, requestInfo)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call_api/<button_id>')
def call_api(button_id):
    if button_id == "1":
        question = "Start script"
    if button_id == "2":
        question = "I'm looking for a pair of new glasses."
    if button_id == "3":
        question = "So I do wear my glasses all day at the computer but also I want something stylish for going out. I am looking for something that is modern, I like bold frames and bright colors"
    if button_id == "4":
        question = "OK. I really like the 3rd one. Can you tell me more about them?"
    if button_id == "5":
        question = "OK. How much are these frames and do you have them in stock?  How long will it take to get them readied?"
    if button_id == "6":
        question = "No, that's all."
    if button_id == "101":
        question = "try on"
    if button_id == "102":
        question = "second one"
    if button_id == "103":
        question = "third one"
    try:
        response = client.query(question)
        decode_string = base64.b64decode(response['AllResults'][0]['ResponseAudioBytes'])
        return Response(decode_string, mimetype='audio/wav')
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True) 