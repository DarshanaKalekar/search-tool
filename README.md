# BharatX Product Price Search Tool

## Overview
This project is a full-stack solution to fetch the price of a given product from multiple websites, based on the country and product query. It uses a generic approach with Google Custom Search API to find product links and extract prices, and provides a minimal React UI for easy use.

---

## Features
- **Backend:** FastAPI (Python)
- **Frontend:** React + Vite
- **Generic scraping:** Uses Google Custom Search API to find product links from any e-commerce site
- **Price extraction:** Uses regex/heuristics to extract price and product name
- **Results:** Sorted by price, with product name, price, currency, and link

---

## Setup Instructions

### 1. Clone the repository
```bash
# In your desired directory
# git clone <repo-url>
cd bharatX
```

### 2. Backend Setup (FastAPI)
- Make sure you have Python 3.8+
- Install dependencies:
```bash
pip install -r requirements.txt
```
- Start the backend server:
```bash
uvicorn app.main:app --reload
```
- The API will be available at `http://localhost:8000`

### 3. Frontend Setup (React + Vite)
- In a new terminal, go to the frontend directory:
```bash
cd frontend
npm install
npm run dev
```
- The app will be available at the URL shown in the terminal (usually `http://localhost:5173`)

---

## Usage
- Open the frontend in your browser.
- Enter a country (e.g., IN, US) and a product query (e.g., "iPhone 16 Pro, 128GB").
- Click "Search" to see results from multiple sites, sorted by price.

---

## API Details
### POST `/search`
**Request Body:**
```json
{
  "country": "IN",
  "query": "boAt Airdopes 311 Pro"
}
```
**Response:**
```json
[
  {
    "link": "https://www.flipkart.com/...",
    "price": 999,
    "currency": "INR",
    "productName": "boAt Airdopes 311 Pro ...",
    "parameters": {}
  },
  ...
]
```

---

## Configuration
- The backend uses Google Custom Search API. You must set your API key and CSE ID in `app/scrapers/generic_search.py`.
- Make sure your CSE is set to "Search the entire web" for best results.

---

## Notes
- This is a demo/prototype. Price extraction uses regex and may not work for all sites.
- For production, consider using LLMs or more advanced extraction methods.
- You can add more regex patterns or improve extraction logic as needed.

---

## License
MIT 