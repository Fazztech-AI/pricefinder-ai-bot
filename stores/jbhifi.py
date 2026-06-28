from urllib.parse import quote_plus
from playwright.sync_api import sync_playwright

def search(query):
    search_url = f"https://www.jbhifi.com.au/search?query={quote_plus(query)}"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(search_url, wait_until="networkidle", timeout=30000)

            text = page.inner_text("body")
            browser.close()

        return [{
            "store": "JB Hi-Fi",
            "query": query,
            "title": "JB Hi-Fi rendered search",
            "price": None,
            "unit_price": None,
            "url": search_url,
            "confidence": "Medium",
            "note": text[:1000],
            "debug_preview": text[:300]
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
