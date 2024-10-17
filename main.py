import requests

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_github_user(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

import requests

def get_random_cat_image(api_key):
    url = 'https://api.thecatapi.com/v1/images/search'
    headers = {'x-api-key': api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()[0]['url']
    else:
        return None
