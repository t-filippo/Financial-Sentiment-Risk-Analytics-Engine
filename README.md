# Financial Sentiment & Risk Analytics Engine

A Python-based OSINT research engine that combines real-time news sentiment 
and financial fundamentals to identify and rank high-potential tech/AI stocks.

## Hypothesis
Public sentiment extracted from real-time financial news 
contains measurable signals that reflect market perception 
of a stock before it is priced in. By aggregating and scoring 
sentiment across multiple sources, it is possible to identify 
stocks with consistently positive or negative momentum.

## Methodology
The user inputs a stock ticker. The system fetches real-time 
news articles via Alpha Vantage and financial fundamentals 
(revenue, EPS, net income) via Financial Modeling Prep. 
A composite sentiment score is calculated by averaging 
individual article sentiment scores returned by the API. 
Stocks are then ranked by composite score to identify 
the highest-sentiment candidates for further analysis.

## Results
System tested on real tickers including NVDA.
Output per ticker:
- Composite sentiment score across recent news articles
- Financial fundamentals: revenue, EPS, net income
- Ranked sentiment comparison across multiple tickers

Sample — NVDA output:
- Sentiment Score: 0.337511
- Revenue:  215938000000
- EPS: 4.93

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

## What didn't work
- Initial approach used multiple API calls per session, 
  which exhausted free tier limits rapidly. Switched to 
  cached examples and minimal calls during development 
  to preserve quota.
- Composite scoring based purely on article count average 
  does not weight article recency or source reliability. 
  Known limitation to address in next iteration.

## Limitations
- Input validation is minimal — unexpected ticker formats 
  or invalid symbols may cause unhandled errors.
- Sentiment scores depend entirely on Alpha Vantage API 
  quality and availability.
- No historical backtesting — sentiment signal has not 
  been validated against actual price movement.
- Risk analytics module not yet implemented.
- Free API tier limits real-time usage in production.

  
## Setup
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your API keys
5. Run: `python main/main.py`

## Author
Filippo Todoroff — 16 y/o | Switzerland  
Building toward Quant Research | github.com/t-filippo
