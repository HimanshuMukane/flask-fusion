def generate_carousel(items):
    carousel_items = []

    for i, item in enumerate(items):
        active_class = "is-selected" if i == 0 else ""
        image_path = f"/static/images/{item['image']}"
        text_content = item.get('text_content', f'Image {i + 1}')
        # caption = item.get('caption', f'Image {i + 1}')
        # description = item.get('description', '')

        carousel_items.append(f"""
            <li class="carousel_slide {active_class}">
          <div class="carousel_image">
            <img src="{image_path}" alt="" role="presentation">
          </div>
          <h2 class="carousel_title">{text_content}</h2>
        </li>
        """)

    carousel_code = f"""
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/HimanshuMukane/cssandjsdump@main/css/Carousel.css">
         <main class="main">
  <div class="carousel">
    <button type="button" class="carousel_btn jsPrev" aria-label="Previous slide">
      <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" />
      </svg>
    </button>

    <div class="carousel_track-container">
      <ul class="carousel_track">
        {"".join(carousel_items)}
      </ul>
    </div>

    <button type="button" class="carousel_btn jsNext" aria-label="Next slide">
      <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" />
      </svg>
    </button>
  </div>
</main>
<script src="https://cdn.jsdelivr.net/gh/HimanshuMukane/cssandjsdump@main/js/Carousel.js"></script>

    """

    return carousel_code
