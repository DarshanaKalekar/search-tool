from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.utils import is_product_match
import time

def scrape_amazon(query: str, country: str) -> list:
    options = Options()
    # options.add_argument('--headless')  # Remove headless for debugging
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    domain = 'com' if country == 'US' else 'in'
    url = f'https://www.amazon.{domain}/s?k={query.replace(" ", "+")}'
    print(f"Navigating to: {url}")
    driver.get(url)
    time.sleep(5)  # Increased wait time
    results = []
    products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
    print(f"Found {len(products)} products on Amazon.")
    for product in products[:8]:
        try:
            title_elem = product.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
            price_whole = product.find_element(By.XPATH, ".//span[@class='a-price-whole']")
            price_frac = product.find_element(By.XPATH, ".//span[@class='a-price-fraction']")
            link_elem = product.find_element(By.XPATH, ".//a[@class='a-link-normal s-no-outline']")
            title = title_elem.text.strip()
            price = float(price_whole.text.replace(',', '') + '.' + price_frac.text)
            link = link_elem.get_attribute('href')
            print(f"Product: {title}, Price: {price}, Link: {link}")
            if is_product_match(query, title, threshold=60):
                results.append({
                    "link": link,
                    "price": price,
                    "currency": "USD" if country == 'US' else "INR",
                    "productName": title,
                    "parameters": {}
                })
        except Exception as e:
            print(f"Error parsing product: {e}")
            continue
    driver.quit()
    return results
