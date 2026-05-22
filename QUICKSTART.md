# Quick Start Guide

Get the Financial Sentiment & Risk Analytics Engine running 
in under 10 minutes.

## Prerequisites
- Python 3 installed
- Git installed
- Alpha Vantage API key (free at alphavantage.co)
- Financial Modeling Prep API key (free at financialmodelingprep.com)

## Step 1 — Clone the repository
```bash
git clone https://github.com/t-filippo/Financial-Sentiment-Risk-Analytics-Engine
cd Financial-Sentiment-Risk-Analytics-Engine
```

## Step 2 — Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

## Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

## Step 4 — Configure API keys
```bash
cp .env.example .env
```
Open `.env` and add your keys:

ALPHA_VANTAGE_API_KEY=your_key_here

FMP_API_KEY=your_key_here


## Step 5 — Run the program
```bash
python3 main/main.py
```

## Step 6 — Enter a ticker
When prompted, enter a stock ticker:

Enter ticker: NVDA

## Expected output

    Sentiment Score: 0.337511
    Revenue: 215938000000
    EPS: 4.93


## Common issues
**ModuleNotFoundError** — make sure you activated 
the virtual environment (Step 2)

**API Error** — check your API keys in the .env file

## Free API limits
Both APIs have free tiers with rate limits.
If you hit limits, wait 1 minute and retry.


