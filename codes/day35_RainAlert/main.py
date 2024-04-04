import requests

WEATHER_KEY = 'YOURKEYHERE'
LOCATION = 'YOURLOCATIONHERE'
TELEGRAM_BOT_API_KEY = 'YOURBOTKEY'
TELEGRAM_CHAT_ID = 'YOURCHATID'

def send_telegram_message(message):
    telegram_bot_api_key = TELEGRAM_BOT_API_KEY
    url = f"https://api.telegram.org/bot{telegram_bot_api_key}/sendMessage"
    telegram_params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.get(url=url, params=telegram_params)
    response.raise_for_status()

weather_params = {
    'key': WEATHER_KEY,
    'q': LOCATION,
    'aqi': 'no',
    'alerts': 'yes',
    'hour': '6,18'
}

response = requests.get(url='https://api.weatherapi.com/v1/forecast.json', params=weather_params)
response.raise_for_status()

forecast_today = response.json()['forecast']['forecastday'][0]['hour']
for hour, forecast in enumerate(forecast_today):
    if hour == 5 and int(forecast['chance_of_rain']) > 50:
        send_telegram_message(f"Bring an umbrella, today might rain on your way to work, chance of rain is {forecast['chance_of_rain']}")
    if hour == 11 and int(forecast['chance_of_rain']) > 50:
        send_telegram_message(f"Bring an umbrella, today might rain on your way to workout, chance of rain is {forecast['chance_of_rain']}")
    if hour == 16 and int(forecast['chance_of_rain']) > 50:
        send_telegram_message(f"Bring an umbrella, today might rain on your way back from work, chance of rain is {forecast['chance_of_rain']}")
