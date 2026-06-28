from datetime import datetime

price_history = []

def save_price_check(result):
    record = {
        "store": result.get("store"),
        "query": result.get("query"),
        "title": result.get("title"),
        "price": result.get("price"),
        "unit_price": result.get("unit_price"),
        "url": result.get("url"),
        "confidence": result.get("confidence"),
        "note": result.get("note"),
        "checked_at": datetime.utcnow().isoformat()
    }

    price_history.append(record)
    return record

def get_price_history():
    return price_history
