from flask import Flask, render_template,request
from library.carousel_routes import carousel_routes
from library.modal_routes import modal_routes
from library.config import loader
app = Flask(__name__)
app.jinja_loader = loader 

carousel_routes(app)
modal_routes(app)

@app.route('/',methods=['GET', 'POST'])
def create():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)