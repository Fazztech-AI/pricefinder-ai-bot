import requests

APP_ID = "VTVKM5URPX"
API_KEY = "1d989f0839a992bbece9099e1b091f07"

URL = f"https://{APP_ID.lower()}-dsn.algolia.net/1/indexes/*/queries"

HEADERS = {
    "X-Algolia-API-Key": API_KEY,
    "X-Algolia-Application-Id": APP_ID,
    "Content-Type": "application/json"
}

def search(query):
    payload = {
        "requests": [
            {
                "indexName": "shopify_products_families",
                "hitsPerPage": 10,
                "query": query,
                "filters": "(price > 0 AND product_published = 1 AND availability.displayProduct = 1)"
            }
        ]
    }

    response = requests.post(URL, headers=HEADERS, json=payload, timeout=10)
    data = response.json()

    hits = data.get("results", [{}])[0].get("hits", [])

    results = []

    for item in hits:
        handle = item.get("handle", "")
        price = item.get("price")
        title = item.get("title", "Unknown product")
        availability = item.get("availability", {}).get("availabilityStatement", "Unknown")

        results.append({
            "store": "JB Hi-Fi",
            "query": query,
            "title": title,
            "price": price,
            "unit_price": None,
            "url": f"https://www.jbhifi.com.au/products/{handle}",
            "confidence": "High",
            "note": availability
        })

    return results