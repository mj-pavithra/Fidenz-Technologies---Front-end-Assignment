from django.shortcuts import render
import requests
import json
from django.http import HttpResponse

def load_city_codes(request):
    file_url = "https://drive.google.com/uc?id=1RsprTXnwRRKq64jo5zJFk-_ycXVf3S7M"
    response = requests.get(file_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Decode the response content as JSON
        data = json.loads(response.text)

        # Assuming 'List' is the key in your JSON structure
        city_list = data.get('List', [])

        # Extract City Codes from the list
        city_codes = [city['CityCode'] for city in city_list]

        # Print for debugging
        print(city_codes)
        print("City Codes Count: ", len(city_codes))

        return render(request, 'citycodes.html', {'cities': city_list})
    else:
        # Handle the case where the request to Google Drive fails
        return render(request, 'error.html', {'error_message': 'Failed to fetch data from Google Drive'})
