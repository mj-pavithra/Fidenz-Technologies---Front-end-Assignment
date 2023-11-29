from django.shortcuts import render
import requests
import json

def get_city_codes_and_weather(request):
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

        # Fetch weather info for the city codes
        api_token = '0d2860a453f79a39b07fff9738ef9d4d'
        city_codes_str = ','.join(city_codes)
        base_url = 'http://api.openweathermap.org/data/2.5/group'
        params = {
            'id': city_codes_str,
            'units': 'metric',
            'appid': api_token
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            weather_data = response.json()
            print(json.dumps(weather_data, indent=4))
            return render(request, 'citycodes.html', {'cities': weather_data.get('list', [])})
        else:
            print(f'Failed to get weather data. Status code: {response.status_code}')
            return render(request, 'error.html', {'error_message': 'Failed to fetch weather data from OpenWeatherMap'})
    else:
        return render(request, 'error.html', {'error_message': 'Failed to fetch data from Google Drive'})
