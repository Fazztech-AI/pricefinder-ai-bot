from stores import jbhifi
from database import save_price_check

def search_prices(query):
    results = []

    results.extend(jbhifi.search(query))

    saved_results = []
    for result in results:
        saved_results.append(save_price_check(result))

    return saved_results
