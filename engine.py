from stores import jbhifi
from stores import mock_store
from database import save_price_check
from ranking import rank_results

def search_prices(query):
    results = []

    results.extend(mock_store.search(query))
    results.extend(jbhifi.search(query))

    ranked_results = rank_results(results)

    saved_results = []
    for result in ranked_results:
        saved_results.append(save_price_check(result))

    return saved_results