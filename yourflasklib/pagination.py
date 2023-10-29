def generate_pagination(current_page, total_pages, base_url):
    pagination_items = []

    for page in range(1, total_pages + 1):
        if page == current_page:
            pagination_items.append(f'<span class="current-page">{page}</span>')
        else:
            pagination_items.append(f'<a href="{base_url}?page={page}">{page}</a>')

    pagination_code = f"""
        <div class="pagination">
            {"".join(pagination_items)}
        </div>
    """

    return pagination_code
