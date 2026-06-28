from dataclasses import dataclass
from typing import Optional

@dataclass
class PriceResult:
    store: str
    query: str
    title: str
    price: Optional[float]
    unit_price: Optional[str]
    url: str
    confidence: str
    note: str
