from flask import render_template

def create_alert(message, alert_type):
    return render_template('yourflasklib/alert.html', message=message, alert_type=alert_type)
