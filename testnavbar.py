from flask import Flask, render_template
from yourflasklib.navbar import generate_navbar

app = Flask(__name__)

# List of navigation links
navbar_links = [
    {'label': 'Home', 'url': '/'},
    {'label': 'About', 'url': '/about'},
    {'label': 'Services', 'url': '/services'},
    {'label': 'Contact', 'url': '/contact'},
]

@app.route('/')
def test_navbar():
    navbar_code = generate_navbar(navbar_links)
    return render_template('navbar.html', navbar_code=navbar_code)

if __name__ == '__main__':
    app.run(debug=True)
