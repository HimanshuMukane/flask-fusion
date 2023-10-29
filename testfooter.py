from flask import Flask, render_template
from yourflasklib.footer import generate_footer

app = Flask(__name__)

# List of image, caption, and description data
categoryitems = [
    {'category_links': 'http://scanfcode.com/category/c-language/', 'category_text': 'C Lang'},
    {'category_links': 'image2.jpg', 'category_text': 'Cityscape 2'},
]
quick_items = [
    {'quick_links': 'http://scanfcode.com/category/c-language/', 'quick_text': 'C Lang'},
    {'quick_links': 'image2.jpg', 'quick_text': 'Cityscape 2'},
]
social_items = [
    {'social_links': 'http://scanfcode.com/category/c-language/', 'social_text': 'C Lang'},
    {'social_links': 'image2.jpg', 'social_text': 'Cityscape 2'},
]
about_item = {'about_content': 'Scanfcode.com CODE WANTS TO BE SIMPLE is an initiative to help the upcoming programmers with the code. Scanfcode focuses on providing the most efficient code or snippets as the code wants to be simple. We will help programmers build up concepts in different programming languages that include C, C++, Java, HTML, CSS, Bootstrap, JavaScript, PHP, Android, SQL and Algorithm.'}
@app.route('/')
def test_footer():
    footer_code = generate_footer(categoryitems,quick_items,social_items,about_item)
    return render_template('footer.html', footer_code=footer_code)

if __name__ == '__main__':
    app.run(debug=True)
