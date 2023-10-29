from flask import Flask, render_template
from yourflasklib.button import generate_button

app = Flask(__name__)

@app.route('/')
def test_button():
    # Example buttons
    primary_button = generate_button('Primary Button', 'btn-primary', 'btn btn-primary', 'alert("Primary button clicked!");')
    secondary_button = generate_button('Secondary Button', 'btn-secondary', 'btn btn-secondary', 'alert("Secondary button clicked!");')
    success_button = generate_button('Success Button', 'btn-success', 'btn btn-success', 'alert("Success button clicked!");')

    return render_template('button.html', primary_button=primary_button, secondary_button=secondary_button, success_button=success_button)

if __name__ == '__main__':
    app.run(debug=True)
