import requests
from datetime import datetime

USERNAME = 'brunoshabitstrackers'
TOKEN = 'dnsiohammbvaksjdubbapqqqq'
GRAPH_NAME = 'graph1'

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
#response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_params = {
    'id': GRAPH_NAME,
    'name': 'reading graph',
    'unit': 'pages',
    'type': 'int',
    'color': 'ajisai'
}
headers = {
    'X-USER-TOKEN': TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

pixel_endpoint = f'{graph_endpoint}/{GRAPH_NAME}'
pixel_params = {
    'date': datetime.now().strftime("%Y%m%d"),
    'quantity':'1'
}
print(pixel_params)
#response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
#print(response.text)