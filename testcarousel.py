from flask import Flask, render_template
from yourflasklib.carousel import generate_carousel

app = Flask(__name__)

# List of image, caption, and description data
items = [
    {'image': 'image1.jpg', 'text_content': 'Nature Scene 1'},
    {'image': 'image2.jpg', 'text_content': 'Cityscape 2'},
    {'image': 'image3.jpg', 'text_content': 'Wildlife 3'},
]

@app.route('/')
def test_carousel():
    carousel_code = generate_carousel(items)
    return render_template('carousel.html', carousel_code=carousel_code)

if __name__ == '__main__':
    app.run(debug=True)
