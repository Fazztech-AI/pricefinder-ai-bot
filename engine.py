from stores import jbhifi
from stores import mock_store
from database import save_price_check

def search_prices(query):
    results = []

    results.extend(mock_store.search(query))
    results.extend(jbhifi.search(query))

    saved_results = []
    for result in results:
        saved_results.append(save_price_check(result))

    saved_results.sort(
        key=lambda x: x["price"] if x["price"] is not None else 999999
    )

    return saved_results
