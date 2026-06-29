def is_relevant(result, query):
    title = result.get("title", "").lower()
    words = query.lower().split()

    return all(word in title for word in words)


def rank_results(results, query=None):
    if query:
        results = [r for r in results if is_relevant(r, query)]

    valid_prices = [r for r in results if r.get("price") is not None]
    no_prices = [r for r in results if r.get("price") is None]

    valid_prices.sort(key=lambda r: r["price"])

    return valid_prices + no_prices