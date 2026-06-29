import requests
from urllib.parse import quote_plus

BUILD_ID = "zD4kjXn477yi7OINsgKZh"

def search(query):
    url = (
        f"https://www.harveynorman.com.au/_next/data/"
        f"{BUILD_ID}/catalogSearch.json?q={quote_plus(query)}"
    )

    response = requests.get(url, timeout=10)
    data = response.json()

    items = data.get("pageProps", {}).get("items", [])

    results = []

    for item in items[:10]:
        price = (
            item.get("price_range", {})
            .get("minimum_price", {})
            .get("final_price", {})
            .get("value")
        )

        url_key = item.get("url_key", "")
        url_suffix = item.get("url_suffix", ".html")

        results.append({
            "store": "Harvey Norman",
            "query": query,
            "title": item.get("name", "Unknown product"),
            "price": price,
            "unit_price": None,
            "url": f"https://www.harveynorman.com.au/{url_key}{url_suffix}",
            "confidence": "High",
            "note": item.get("sku", "")
        })

    return results