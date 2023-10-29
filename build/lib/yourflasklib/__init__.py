# yourflasklib/__init__.py

from flask import Flask
from .components.carousel import create_carousel
from .components.navbar import create_responsive_navbar
from .components.alert import create_alert
from .components.modal import create_modal
from .components.form import create_form
from .components.button import create_button
from .components.card import create_card
from .components.pagination import create_pagination

app = Flask(__name__, template_folder='yourflasklib/templates')

# Register your components as Flask context processors
app.jinja_env.globals.update(create_carousel=create_carousel)
app.jinja_env.globals.update(create_responsive_navbar=create_responsive_navbar)
app.jinja_env.globals.update(create_alert=create_alert)
app.jinja_env.globals.update(create_modal=create_modal)
app.jinja_env.globals.update(create_form=create_form)
app.jinja_env.globals.update(create_button=create_button)
app.jinja_env.globals.update(create_card=create_card)
app.jinja_env.globals.update(create_pagination=create_pagination)
