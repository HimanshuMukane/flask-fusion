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
from .navbar import create_responsive_navbar
from .alert import create_alert
from .modal import create_modal
from .form import create_form
from .button import create_button
from .card import create_card
from .pagination import create_pagination

# Register your components as Flask context processors
app.jinja_env.globals.update(create_carousel=generate_carousel)
app.jinja_env.globals.update(create_responsive_navbar=create_responsive_navbar)
app.jinja_env.globals.update(create_alert=create_alert)
app.jinja_env.globals.update(create_modal=create_modal)
app.jinja_env.globals.update(create_form=create_form)
app.jinja_env.globals.update(create_button=create_button)
app.jinja_env.globals.update(create_card=create_card)
app.jinja_env.globals.update(create_pagination=create_pagination)

# Print the template and static folder paths for debugging
print("Template Folder Path:", app.template_folder)
print("Static Folder Path:", app.static_folder)
