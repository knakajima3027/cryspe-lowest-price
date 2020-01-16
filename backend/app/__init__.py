from flask import Flask, render_template, jsonify
from app.models import Card

app = Flask(__name__)

# カード情報を全て返すAPI
@app.route('/')
def index():
    cards = Card.query.all()

    result = []
    for card in cards:
        result_json = {
            'name': card.card_name,
            'price': card.card_price,
            'img': card.img_url,
            'url': card.url
        }
        result.append(result_json)

    return jsonify(result) 
