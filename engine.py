from stores import jbhifi

def search_prices(query):
    results = []

    results.extend(jbhifi.search(query))

    return results
