import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_KEY")
fmp_key = os.getenv("FMP_KEY")

def get_news_sentiment(clean_ticker, api_key):

    url = "https://www.alphavantage.co/query"

    params = {
        "function": "NEWS_SENTIMENT",
        "tickers": clean_ticker,   
        "apikey": api_key
        }

    r = requests.get(url, params=params)
    data = r.json()
    return(data)

def get_fmp_foundamentals(clean_ticker, fmp_key):

    url_fmp = "https://financialmodelingprep.com/stable/income-statement"

    params = {
        "symbol": clean_ticker,
        "apikey": fmp_key,
    }

    r = requests.get(url_fmp, params=params)
    data = r.json()
    return(data)
    

def parse_sentiment(data, clean_ticker):

    if "feed" not in data:
        print("warning")
        return
    
    for element in data ["feed"][0]["ticker_sentiment"]:
        if element["ticker"] == clean_ticker:
            return element ['relevance_score'], element['ticker_sentiment_score']

def calculate_scores(data, clean_ticker):
    scores = []
    for article in data["feed"]:
        for element in article["ticker_sentiment"]:
            if element["ticker"] == clean_ticker:
                scores.append(float(element["ticker_sentiment_score"]))

    average = sum(scores)/len(scores)
    return(average)

assets = input("Ticker: ").upper()
list_ticker = assets.split(",")
result_1 = {}
for ticker in list_ticker:
    clean_ticker = ticker.strip()
    data = get_news_sentiment(clean_ticker, api_key)

    foundamentals = get_fmp_foundamentals(clean_ticker, fmp_key)

    if not foundamentals: 
        print("warning fmp")
        continue 

    if foundamentals: 
        latest = foundamentals[0]
        
    print("\n" + clean_ticker)
    print("revenue: "+ str(latest.get("revenue")))
    print("netIncome: "+ str(latest.get("netIncome")))
    print("eps: " + str(latest.get("eps")))
    print("operatingIncome: " + str(latest.get("operatingIncome"))) 

    revenue = latest.get("revenue")
    netIncome = latest.get("netIncome")
    eps = latest.get("eps")
    operatingIncome = latest.get("operatingIncome")

    latest_prev = foundamentals[1]
    revenue_prev = latest_prev.get("revenue")
    revenue_growth = (revenue - revenue_prev) / revenue_prev *100
    print("revenue growth %: ", round(revenue_growth, 2))

    result = parse_sentiment(data, clean_ticker)
    if result is None: 
        continue
    relevance, sentiment = result 
    relevance = float(relevance)
    sentiment = float(sentiment)
    average = calculate_scores(data, clean_ticker)
    print("\n" + "relevance: ", relevance)
    print("sentiment: ", sentiment)
    print("average: ", average)
    time.sleep(12)

    result_1[clean_ticker] = {
        "relevance": relevance, 
        "sentiment": sentiment, 
        "average": average, 
        "revenue": revenue, 
        "netIncome": netIncome,
        "eps": eps,
        "operatingIncome": operatingIncome,
        "revenue_growth": revenue_growth
    }

print(result_1)

ranking = sorted(result_1.items(), key=lambda x: x[1]["average"], reverse=True)
for ticker, scores in ranking[:5]:
    print(ticker, scores["average"])
