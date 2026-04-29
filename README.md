# Financial Sentiment & Risk Analytics Engine

A Python-based OSINT research engine that combines real-time news sentiment 
and financial fundamentals to identify and rank high-potential tech/AI stocks.

## What it does
- Fetches real-time news sentiment for any stock ticker via Alpha Vantage
- Retrieves financial fundamentals (revenue, EPS, net income) via FMP
- Calculates a composite sentiment score across multiple news articles
- Ranks stocks by sentiment average to identify top candidates
- Outputs a structured dataset ready for risk analysis

## Tech Stack
- Python 3.12
- requests, python-dotenv
- Alpha Vantage API
- Financial Modeling Prep API

## Setup
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your API keys
5. Run: `python main/main.py`

## Author
Built as a learning project exploring quantitative finance and data engineering.
