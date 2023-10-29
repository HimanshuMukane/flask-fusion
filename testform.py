from flask import Flask, render_template
from yourflasklib.form import generate_form

app = Flask(__name__)

# Form data
form_data = {
    'contact_form': {
        'action': '/submit',
        'method': 'POST',
        'fields': [
            '<label for="name">Name:</label><input type="text" id="name" name="name"><br>',
            '<label for="email">Email:</label><input type="email" id="email" name="email"><br>',
            '<label for="message">Message:</label><textarea id="message" name="message"></textarea><br>',
        ],
    }
}

@app.route('/')
def test_form():
    form_code = generate_form('contact_form', form_data['contact_form']['action'], form_data['contact_form']['method'], form_data['contact_form']['fields'])
    return render_template('form.html', form_code=form_code)

if __name__ == '__main__':
    app.run(debug=True)
