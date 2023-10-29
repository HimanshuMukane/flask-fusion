from flask import render_template

def create_form(fields):
    return render_template('yourflasklib/form.html', fields=fields)
