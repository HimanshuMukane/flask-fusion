from flask import Flask, render_template
from yourflasklib.card import generate_cards

app = Flask(__name__)

# List of card data
card_data = [
    {'title': 'Card 1', 'content': 'This is the first card', 'image': 'card1.jpg'},
    {'title': 'Card 2', 'content': 'This is the second card', 'image': 'card2.jpg'},
    {'title': 'Card 3', 'content': 'This is the third card', 'image': 'card3.jpg'},
]

@app.route('/card')
def test_cards():
    card_code = generate_cards(card_data)
    return render_template('card.html', card_code=card_code)

if __name__ == '__main__':
    app.run(debug=True)
