from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from app.scrapers import generic_search_scraper

app = FastAPI()

# Allow all origins for development (adjust in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    country: str
    query: str

@app.post("/search")
def search_products(request: SearchRequest):
    country = request.country.upper()
    query = request.query
    # Use the generic search scraper for all queries
    results = generic_search_scraper(query, country, num_results=7)
    return results
