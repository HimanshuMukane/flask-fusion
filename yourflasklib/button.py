from flask import render_template

def create_button(text, button_type):
    return render_template('yourflasklib/button.html', text=text, button_type=button_type)
