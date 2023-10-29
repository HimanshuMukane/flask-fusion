from flask import render_template

def create_pagination(total_pages, current_page):
    return render_template('yourflasklib/pagination.html', total_pages=total_pages, current_page=current_page)
