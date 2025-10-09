import requests

API_KEY = "1ac67e2cf4183ab929ab89ba400978cf"

def get_data(place,days=None,kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_days =8*days
    filtered_data = filtered_data[0:nr_days]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Thane",days=1,kind='sky'))
