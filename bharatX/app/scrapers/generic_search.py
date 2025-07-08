import requests
import re
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.environ.get("GOOGLE_CSE_ID")

if not GOOGLE_API_KEY or not GOOGLE_CSE_ID:
    raise RuntimeError("GOOGLE_API_KEY and GOOGLE_CSE_ID must be set as environment variables.")

# Regex patterns for price extraction (₹, $, etc.)
PRICE_PATTERNS = [
    r"₹\s?([0-9,]+)",
    r"Rs\.?\s?([0-9,]+)",
    r"\$\s?([0-9,]+)"
]


def google_search(query, num_results=5):
    url = (
        f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}"
        f"&cx={GOOGLE_CSE_ID}&q={requests.utils.quote(query)}&num={num_results}"
    )
    resp = requests.get(url)
    data = resp.json()
    print("Google API response:", data)
    links = []
    for item in data.get("items", []):
        links.append(item["link"])
    print("Links found:", links)
    return links


def extract_price(text):
    for pattern in PRICE_PATTERNS:
        match = re.search(pattern, text)
        if match:
            price = match.group(1).replace(",", "")
            try:
                return float(price)
            except Exception:
                continue
    return None


def extract_product_info(url):
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.title.text.strip() if soup.title else url
        price = None
        # Try to find price in visible text
        for tag in soup.find_all(text=True):
            price = extract_price(tag)
            if price:
                break
        # Try to guess currency
        currency = "INR" if "₹" in resp.text or ".in" in url else "USD"
        info = {
            "link": url,
            "price": price,
            "currency": currency,
            "productName": title,
            "parameters": {}
        }
        print(f"Extracted info for {url}: {info}")
        return info
    except Exception as e:
        print(f"Error extracting info from {url}: {e}")
        return None


def generic_search_scraper(query, country, num_results=5):
    search_query = f"{query} {country}"
    links = google_search(search_query, num_results=num_results)
    results = []
    for link in links:
        info = extract_product_info(link)
        if info and info["price"]:
            results.append(info)
    # Sort by price
    results = sorted(results, key=lambda x: x["price"])
    print("Final results:", results)
    return results 