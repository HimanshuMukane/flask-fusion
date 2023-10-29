def generate_footer(categoryitems, quick_items, social_items, about_item):
    about_content = f"{about_item['about_content']}"

    category_items = []
    quick_items = []
    social_items = []

    for item in categoryitems:
        category_links = f"{item['category_links']}"
        category_text = item['category_text']
        category_items.append(f"""
        <ul class="footer-links">
              <li><a href="{category_links}">{category_text}</a></li>
        </ul>
        """)
    
    for item in quick_items:
        quick_links = f"{item['quick_links']}"
        quick_text = item.get('quick_text', f'Image {i + 1}')
        quick_items.append(f"""
        <ul class="footer-links">
              <li><a href="{quick_links}">{quick_text}</a></li>
        </ul>
        """)
    
    for item in social_items:
        social_links = f"{item['social_links']}"
        social_text = item.get('social_text', f'Image {i + 1}')
        social_items.append(f"""
        <ul class="footer-links">
              <li><a href="{social_links}">{social_text}</a></li>
        </ul>
        """)

    footer_code = f"""
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"/>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
 <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/HimanshuMukane/cssandjsdump@main/css/footer.css"/>
  
    <footer class="site-footer">
      <div class="container">
        <div class="row">
          <div class="col-sm-12 col-md-6">
            <h6>About</h6>
            <p class="text-justify">
            {"".join(about_content)}
            </p>
          </div>

          <div class="col-xs-6 col-md-3">
            <h6>Categories</h6>
            <ul class="footer-links">
            {"".join(category_items)}
            </ul>
          </div>

          <div class="col-xs-6 col-md-3">
            <h6>Quick Links</h6>
            <ul class="footer-links">
            {"".join(quick_items)}
            </ul>
          </div>
        </div>
        <hr>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-md-8 col-sm-6 col-xs-12">
            <p class="copyright-text">Copyright &copy; 2017 All Rights Reserved by 
            </p>
          </div>

          <div class="col-md-4 col-sm-6 col-xs-12">
            <ul class="social-icons">
            {"".join(social_items)}

            </ul>
          </div>
        </div>
      </div>
</footer>

    """

    return footer_code
