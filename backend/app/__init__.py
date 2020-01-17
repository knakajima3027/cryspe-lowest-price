from flask import Flask, render_template, jsonify, request
from app.models import Card
from app.config import session

app = Flask(__name__, static_folder='../../frontend/dist/static', template_folder='../../frontend/dist')


@app.route('/api')
def card():
    name = request.args.get('card_name')
    price = request.args.get('card_price')
    cards = Card.query.filter(Card.card_price<=price, Card.card_name.like( "%%%s%%" %   name)).all()

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

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


