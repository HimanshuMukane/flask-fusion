def generate_navbar(nav_links):
    nav_items = []

    for link in nav_links:
        label = link.get('label', 'Link')
        url = link.get('url', '#')

        nav_items.append(f'<a href="{url}">{label}</a>')

    navbar_code = f"""
        <nav>
            <ul>
                {"".join(nav_items)}
            </ul>
        </nav>
  <link rel="stylesheet" href="yourflasklib\static\css\nav.css">

        <div class="nav">
  <input type="checkbox" id="nav-check">
  <div class="nav-header">
    <div class="nav-title">
      JoGeek
    </div>
  </div>
  <div class="nav-btn">
    <label for="nav-check">
      <span></span>
      <span></span>
      <span></span>
    </label>
  </div>
  
  <div class="nav-links">
    <a href="//github.io/jo_geek" target="_blank">Github</a>
    <a href="http://stackoverflow.com/users/4084003/" target="_blank">Stackoverflow</a>
    <a href="https://in.linkedin.com/in/jonesvinothjoseph" target="_blank">LinkedIn</a>
    <a href="https://codepen.io/jo_Geek/" target="_blank">Codepen</a>
    <a href="https://jsfiddle.net/user/jo_Geek/" target="_blank">JsFiddle</a>
  </div>
</div>
<style>
    """

    return navbar_code
