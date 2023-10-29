from flask import render_template

def create_modal(title, content):
    return render_template('yourflasklib/modal.html', title=title, content=content)
