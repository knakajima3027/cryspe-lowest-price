from flask import Flask, render_template, jsonify
from app.models import Card

app = Flask(__name__, static_folder='../../frontend/dist/static', template_folder='../../frontend/dist')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    '''
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
    '''
    return render_template('index.html')
