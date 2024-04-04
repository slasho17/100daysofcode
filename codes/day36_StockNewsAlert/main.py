import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_APIKEY = 'yourapikey'
NEWS_APIKEY = 'yourapikey'

TELEGRAM_BOT_API_KEY = 'yourapikey'
TELEGRAM_CHAT_ID = 'yourchatid'

alphavantage_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'
alphavantage_params = {
    'symbol': STOCK,
    'apikey': ALPHAVANTAGE_APIKEY
}
response = requests.get(url=alphavantage_url, params=alphavantage_params)
response.raise_for_status()

data = response.json()
latest_data = data['Time Series (Daily)']
latest_date = max(latest_data.keys())
yesterday_date = max(dt for dt in latest_data.keys() if dt < latest_date)
day_before_yesterday_date = max(dt for dt in latest_data.keys() if dt < yesterday_date)

closing_price_yesterday = float(latest_data[yesterday_date]['4. close'])
closing_price_day_before_yesterday = float(latest_data[day_before_yesterday_date]['4. close'])

difference = closing_price_yesterday - closing_price_day_before_yesterday

print(f"Closing price for the end of yesterday: {closing_price_yesterday}")
print(f"Closing price for the end of the day before yesterday: {closing_price_day_before_yesterday}")

if abs(difference) > closing_price_yesterday * 0.05:

    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'

    # Specify the stock symbol of the company you're interested in
    stock_symbol = 'AAPL'

    # Construct the URL
    url = f'https://newsapi.org/v2/everything?q={STOCK}&apiKey={NEWS_APIKEY}&pageSize=3&sortBy=publishedAt'

    # Make the request
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()

    # Extract and print information about each article
    articles = data['articles']
    for article in articles:
        title = article['title']
        source = article['source']['name']
        description = article['description']
        published_at = article['publishedAt']
        arrow = '🔺' if difference > 0 else '🔻'

        message = f'''
            {STOCK}: {arrow}{(abs(difference)/100) * closing_price_yesterday}%
            Title: {title}
            Source: {source}
            Published At: {published_at}
            {description}
            '''
        
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/sendMessage"
        telegram_params = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message
        }
        response = requests.get(url=url, params=telegram_params)
        response.raise_for_status()


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

