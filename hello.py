from flask import Flask, render_template, jsonify, request, abort
import json
from textblob import TextBlob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

app.debug = True

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/api/v1.0/sentiment', methods=['POST'])
def receive_scan_from_api():
# Example at Heroku:
# curl -X POST -H 'Content-Type: application/json' -d '{"data":"Are you kidding me? This is GREAT!"}' https://sentiment-fryan.herokuapp.com/api/v1.0/sentiment
    if not request.json:
        abort(400)
    
    print (request.json)

    sentence = TextBlob(request.json['data'])

    return jsonify({'Response':sentence.sentiment}), 201


if __name__ == '__main__':
    app.run()

