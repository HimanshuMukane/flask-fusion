def generate_carousel(items):
    carousel_items = []

    for i, item in enumerate(items):
        active_class = "active" if i == 0 else ""
        image_path = f"/static/images/{item['image']}"
        caption = item.get('caption', f'Image {i + 1}')

        carousel_items.append(f"""
            <div class="carousel-item {active_class}">
                <img src="{image_path}" class="d-block w-100" alt="{caption}">
                <div class="carousel-caption d-none d-md-block">
                    <h5>{caption}</h5>
                    <p>{item.get('description', '')}</p>
                </div>
            </div>
        """)

    carousel_code = f"""
    <div id="carouselExample" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
            {"".join(carousel_items)}
        </div>
        <a class="carousel-control-prev" href="#carouselExample" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExample" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
    """

    return carousel_code
