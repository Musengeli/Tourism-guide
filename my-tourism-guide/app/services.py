import requests

API_URL = 'https://freetestapi.com/api/v1/destinations'

def get_destinations():
    response = requests.get(API_URL)
    return response.json()

def get_destination_by_id(id):
    response = requests.get(f'{API_URL}/{id}')
    return response.json()

def search_destinations(query):
    response = requests.get(f'{API_URL}?search={query}')
    return response.json()
