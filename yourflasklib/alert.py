def generate_alert(alert_type, message):
    alert_code = f"""
        <div class="alert {alert_type}">
            {message}
        </div>
    """

    return alert_code
