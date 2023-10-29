def generate_button(label, button_id, button_class, onclick):
    button_code = f"""
        <button id="{button_id}" class="{button_class}" onclick="{onclick}">
            {label}
        </button>
    """

    return button_code
