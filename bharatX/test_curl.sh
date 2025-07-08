#!/bin/bash
# Test for iPhone 16 Pro, 128GB (US)
curl -X POST "http://localhost:8000/search" -H "Content-Type: application/json" -d '{"country": "US", "query": "iPhone 16 Pro, 128GB"}'
# Test for boAt Airdopes 311 Pro (IN)
curl -X POST "http://localhost:8000/search" -H "Content-Type: application/json" -d '{"country": "IN", "query": "boAt Airdopes 311 Pro"}'
