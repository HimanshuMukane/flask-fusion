def generate_modal(modal_id, title, content):
    modal_code = f"""
        <div class="modal" id="{modal_id}">
            <div class="modal-content">
                <div class="modal-header">
                    <span class="modal-close" id="close-{modal_id}">&times;</span>
                    <h2>{title}</h2>
                </div>
                <div class="modal-body">
                    {content}
                </div>
            </div>
        </div>
    """

    return modal_code
