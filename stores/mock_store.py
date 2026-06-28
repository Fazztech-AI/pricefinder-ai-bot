def search(query):
    products = [
        {
            "store": "JB Hi-Fi",
            "query": query,
            "title": "PlayStation 5 Console",
            "price": 799.00,
            "unit_price": None,
            "url": "https://www.jbhifi.com.au/",
            "confidence": "Demo",
            "note": "Mock product data"
        },
        {
            "store": "Big W",
            "query": query,
            "title": "PlayStation 5 Console",
            "price": 749.00,
            "unit_price": None,
            "url": "https://www.bigw.com.au/",
            "confidence": "Demo",
            "note": "Mock product data"
        },
        {
            "store": "Amazon AU",
            "query": query,
            "title": "PlayStation 5 Console",
            "price": 729.00,
            "unit_price": None,
            "url": "https://www.amazon.com.au/",
            "confidence": "Demo",
            "note": "Mock product data"
        }
    ]

    query_lower = query.lower()

    if "ps5" in query_lower or "playstation" in query_lower:
        return products

    return []
