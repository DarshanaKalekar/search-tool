# BharatX Product Price Fetcher

## Overview
This tool fetches the price of a given product from multiple websites based on the country and product query. It returns a list of results sorted by price.

## Setup

1. **Clone the repo**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the API**
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

### Example curl request

#### For iPhone 16 Pro, 128GB (US):
```bash
curl -X POST "http://localhost:8000/search" -H "Content-Type: application/json" -d '{"country": "US", "query": "iPhone 16 Pro, 128GB"}'
```

#### For boAt Airdopes 311 Pro (IN):
```bash
curl -X POST "http://localhost:8000/search" -H "Content-Type: application/json" -d '{"country": "IN", "query": "boAt Airdopes 311 Pro"}'
```

## Docker
To run with Docker:
```bash
docker build -t bharatx-price-fetcher .
docker run -p 8000:8000 bharatx-price-fetcher
```

## Notes
- This is a demo. Real scraping logic should be implemented for production use.
- Add more scrapers in `app/scrapers/` and update `app/config.py` for more countries/sites.
