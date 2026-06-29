import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def search(query):
    url = f"https://www.jbhifi.com.au/search?query={quote_plus(query)}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    return [{
        "store": "JB Hi-Fi",
        "query": query,
        "title": "JB Hi-Fi search page",
        "price": None,
        "unit_price": None,
        "url": url,
        "confidence": "Low",
        "note": "Real JB page checked. Price extraction next."
    }]