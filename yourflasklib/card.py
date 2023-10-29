def generate_cards(card):
    card_items = []

    for card in card:
        title = card.get('title', 'Card Title')
        content = card.get('content', 'Card Content')
        image = card.get('image', '')

        card_items.append(f"""
            <div class="card">
                <img src="{image}" alt="Card Image">
                <div class="card-content">
                    <h3 class="card-title">{title}</h3>
                    <p class="card-text">{content}</p>
                </div>
            </div>
        """)

    card_code = "".join(card_items)

    return card_code
