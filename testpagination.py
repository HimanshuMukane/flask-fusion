from flask import Flask, render_template, request
from yourflasklib.pagination import generate_pagination

app = Flask(__name__)

@app.route('/')
def test_pagination():
    # Example pagination data
    current_page = int(request.args.get('page', 1))
    total_pages = 10
    base_url = '/results'

    pagination_code = generate_pagination(current_page, total_pages, base_url)

    return render_template('pagination.html', pagination_code=pagination_code)

if __name__ == '__main__':
    app.run(debug=True)
