from flask import render_template

def create_responsive_navbar(links):
    return render_template('yourflasklib/navbar.html', links=links)
