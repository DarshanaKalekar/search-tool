from fuzzywuzzy import fuzz

def is_product_match(query: str, product_name: str, threshold: int = 80) -> bool:
    """Return True if the product_name matches the query above a threshold."""
    return fuzz.token_set_ratio(query.lower(), product_name.lower()) >= threshold

# Placeholder for currency conversion

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    # Implement currency conversion logic or use an API
    return amount
