from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='yourflasklib/templates', static_folder='yourflasklib/static')

# Configure the template folder explicitly
app.config['TEMPLATES_AUTO_RELOAD'] = True  # For development, to auto-reload templates
app.template_folder = os.path.join(os.path.dirname(__file__), 'templates')

# Configure the template folder explicitly
app.config['STATIC_AUTO_RELOAD'] = True  # For development, to auto-reload templates
app.static_folder = os.path.join(os.path.dirname(__file__), 'static')

# Import your components and register them as context processors
from .carousel import generate_carousel
from .navbar import generate_navbar
from .alert import generate_alert
from .modal import generate_modal
from .form import generate_form
from .button import generate_button
from .card import generate_cards
from .pagination import generate_pagination

# Register your components as Flask context processors
app.jinja_env.globals.update(create_carousel=generate_carousel)
app.jinja_env.globals.update(generate_navbar=generate_navbar)
app.jinja_env.globals.update(generate_alert=generate_alert)
app.jinja_env.globals.update(generate_modal=generate_modal)
app.jinja_env.globals.update(generate_form=generate_form)
app.jinja_env.globals.update(generate_button=generate_button)
app.jinja_env.globals.update(generate_cards=generate_cards)
app.jinja_env.globals.update(generate_pagination=generate_pagination)

# Print the template and static folder paths for debugging
print("Template Folder Path:", app.template_folder)
print("Static Folder Path:", app.static_folder)
