import requests

API_KEY = "1ac67e2cf4183ab929ab89ba400978cf"

def get_data(place,days=None,kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    filtered_data = filtered_data[0:8*days]
    if kind == 'Temperature':
        filtered_data = [dict['main']['temp'] for data in filtered_data]
    if kind == "sky":
        filtered_data = [dict["weather"]["main"] for data in filtered_data]

    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Thane"))
