import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.utils import is_product_match
import time

def scrape_flipkart(query: str) -> list:
    options = Options()
    # options.add_argument('--headless')  # Remove headless for debugging
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    url = f'https://www.flipkart.com/search?q={query.replace(" ", "+")}'
    print(f"Navigating to: {url}")
    driver.get(url)
    time.sleep(5)  # Increased wait time
    results = []
    products = driver.find_elements(By.XPATH, '//div[contains(@class, "_1AtVbE")]//div[contains(@class, "_13oc-S")]')
    print(f"Found {len(products)} products on Flipkart.")
    for product in products[:8]:
        try:
            title_elem = product.find_element(By.XPATH, ".//div[@class='_4rR01T']")
            price_elem = product.find_element(By.XPATH, ".//div[@class='_30jeq3 _1_WHN1']")
            link_elem = product.find_element(By.XPATH, ".//a")
            title = title_elem.text.strip()
            price = float(price_elem.text.replace('₹', '').replace(',', '').strip())
            link = link_elem.get_attribute('href')
            if link is None:
                continue
            if not link.startswith('http'):
                link = 'https://www.flipkart.com' + link
            print(f"Product: {title}, Price: {price}, Link: {link}")
            if is_product_match(query, title, threshold=60):
                results.append({
                    "link": link,
                    "price": price,
                    "currency": "INR",
                    "productName": title,
                    "parameters": {}
                })
        except Exception as e:
            print(f"Error parsing product: {e}")
            continue
    driver.quit()
    return results
