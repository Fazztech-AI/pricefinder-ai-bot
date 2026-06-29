def rank_results(results):
    valid_prices = [
        r for r in results
        if r.get("price") is not None
    ]

    no_prices = [
        r for r in results
        if r.get("price") is None
    ]

    valid_prices.sort(key=lambda r: r["price"])

    return valid_prices + no_prices