from flask import Flask, jsonify, render_template, request
from backend import get_data

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/find/')
def find():
    videourl = request.args.get('url')
    if not videourl:
        return {"responseMessage": "No video URL provideda"}, 400
    return get_data(videourl)