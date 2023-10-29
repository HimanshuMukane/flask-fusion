from flask import Flask, render_template
from yourflasklib.alert import generate_alert

app = Flask(__name__)

@app.route('/')
def test_alert():
    # Example alert messages
    success_alert = generate_alert('alert-success', 'Operation was successful.')
    info_alert = generate_alert('alert-info', 'This is an informational message.')
    warning_alert = generate_alert('alert-warning', 'Warning: Something may require your attention.')
    error_alert = generate_alert('alert-error', 'An error occurred. Please try again.')

    return render_template('alert.html', success_alert=success_alert, info_alert=info_alert, warning_alert=warning_alert, error_alert=error_alert)

if __name__ == '__main__':
    app.run(debug=True)
