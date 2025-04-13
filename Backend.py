import requests

key = "f5a05521f1ec9b12eccbd5d055af6727"
def get_data(place, days):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={key}'
    response = requests.get(url)
    content = response.json()
    filtered = content["list"]
    filtered = filtered[:8*days]
    return filtered

if __name__ == "__main__":
    get_data()
