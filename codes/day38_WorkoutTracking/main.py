import requests
from datetime import datetime
import json

NUTRITIONIX_APP_ID = 'add_yours_here'
NUTRITIONIX_API_KEY = 'add_yours_here'
NUTRITIONIX_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
NUTRITIOXIN_HEADER = {
    'Content-Type': 'application/json',
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY
}


SHEET_ID = 'myWorkouts'
SHEET_ENDPOINT = 'workouts'
SHEETY_APP_ID = 'add_yours_here'
SHEETY_URL = f'https://api.sheety.co/{SHEETY_APP_ID}/{SHEET_ID}/{SHEET_ENDPOINT}'
SHEETY_HEADERS = {
    'Content-Type': 'application/json',
}


def get_time():
    dt = datetime.now()
    date_string = dt.strftime('%d/%m/%Y')
    time_string = dt.strftime('%H:%M:%S')
    return (date_string, time_string)

def natural_language_requests(query):
    nutri_parms = {
        'query': query    
    }
    response = requests.post(url=NUTRITIONIX_URL, json=nutri_parms, headers=NUTRITIOXIN_HEADER)
    response.raise_for_status()
    
    exers = response.json()['exercises'][0]
    return (exers['name'], exers['duration_min'], exers['nf_calories'])

def sheety_post(workout_info, time):
    # Data for the new row
    data = {
        "workout": {
            "date": time[0],
            "time": time[1],
            "exercise": workout_info[0],
            "duration": workout_info[1],
            "calories": workout_info[2]
        }
    }

    # Make a POST request to add the row
    response = requests.post(SHEETY_URL, headers=SHEETY_HEADERS, json=data)
    response.raise_for_status()
    print(response.json())

        
while (ans := input("Tell me your workout or quit\n")) != 'quit':
    workout_info = natural_language_requests(ans)
    time = get_time()
    sheety_post(workout_info, time)
    

