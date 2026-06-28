import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def search(query):
    search_url = f"https://www.jbhifi.com.au/search?query={quote_plus(query)}"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        page_text = soup.get_text(" ", strip=True)

        return [{
            "store": "JB Hi-Fi",
            "query": query,
            "title": "JB Hi-Fi search result",
            "price": None,
            "unit_price": None,
            "url": search_url,
            "confidence": "Low",
            "note": "Page loads, but prices need API extraction next.",
            "debug_preview": page_text[:300]
        }]
    except Exception as e:
        return [{
            "store": "JB Hi-Fi",
            "query": query,
            "title": "Search failed",
            "price": None,
            "unit_price": None,
            "url": search_url,
            "confidence": "Failed",
            "note": str(e),
            "debug_preview": ""
        }]
