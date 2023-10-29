def generate_form(form_id, action, method, fields):
    form_code = f"""
        <form id="{form_id}" action="{action}" method="{method}">
            {"".join(fields)}
            <input type="submit" value="Submit">
        </form>
    """

    return form_code
