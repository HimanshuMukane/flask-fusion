from flask import Flask, render_template
from yourflasklib.modal import generate_modal

app = Flask(__name__)

# Modal data
modal_data = {
    'modal1': {'title': 'Modal 1', 'content': 'This is the content of Modal 1'},
    'modal2': {'title': 'Modal 2', 'content': 'This is the content of Modal 2'},
}

@app.route('/')
def test_modal():
    modals = []
    for modal_id, data in modal_data.items():
        modal_code = generate_modal(modal_id, data['title'], data['content'])
        modals.append(modal_code)

    return render_template('modal.html', modals=modals)

if __name__ == '__main__':
    app.run(debug=True)
