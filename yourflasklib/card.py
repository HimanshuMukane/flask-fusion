from flask import render_template

def create_card(title, content):
    return render_template('yourflasklib/card.html', title=title, content=content)
