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
    if not request.json:
        abort(400)
    
    print (request.json)

    sentence = TextBlob(request.json['data'])

    return jsonify({'Response':sentence.sentiment}), 201


if __name__ == '__main__':
    app.run()

