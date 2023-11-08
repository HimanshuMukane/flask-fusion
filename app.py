from flask import Flask, render_template,request
from flask_fusion.carousel_routes import carousel_routes
from flask_fusion.modal_routes import modal_routes
from flask_fusion.config import loader
app = Flask(__name__)
app.jinja_loader = loader 

carousel_routes(app)
modal_routes(app)

@app.route('/',methods=['GET', 'POST'])
def create():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)