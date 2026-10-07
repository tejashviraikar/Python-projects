import requests


# ----------------------------
# Get Latitude & Longitude
# ----------------------------
def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if "results" not in data:
            return None

        location = data["results"][0]

        return (
            location["latitude"],
            location["longitude"],
            location["name"],
            location["country"]
        )

    except requests.exceptions.RequestException:
        return None


# ----------------------------
# Get Weather
# ----------------------------
def get_weather(latitude, longitude):

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,"
        f"wind_speed_10m,weather_code"
    )

    response = requests.get(url)
    response.raise_for_status()

    return response.json()


# ----------------------------
# Weather Code
# ----------------------------
def weather_description(code):

    weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing Rime Fog",
        51: "Light Drizzle",
        53: "Moderate Drizzle",
        55: "Dense Drizzle",
        61: "Slight Rain",
        63: "Moderate Rain",
        65: "Heavy Rain",
        71: "Light Snow",
        73: "Moderate Snow",
        75: "Heavy Snow",
        80: "Rain Showers",
        95: "Thunderstorm"
    }

    return weather_codes.get(code, "Unknown")


# ----------------------------
# Main Program
# ----------------------------
def main():

    print("=" * 45)
    print("        WEATHER APPLICATION")
    print("=" * 45)

    while True:

        city = input("\nEnter City Name: ").strip()

        if city == "":
            print("City cannot be empty.")
            continue

        try:

            location = get_coordinates(city)

            if location is None:
                print("City not found.")
                continue

            latitude, longitude, city_name, country = location

            weather = get_weather(latitude, longitude)

            current = weather["current"]

            print("\n========== WEATHER REPORT ==========")
            print(f"City        : {city_name}, {country}")
            print(f"Temperature : {current['temperature_2m']} °C")
            print(f"Humidity    : {current['relative_humidity_2m']} %")
            print(f"Wind Speed  : {current['wind_speed_10m']} km/h")
            print(f"Weather     : {weather_description(current['weather_code'])}")
            print("====================================")

        except requests.exceptions.ConnectionError:
            print("No Internet Connection.")

        except requests.exceptions.Timeout:
            print("Request Timed Out.")

        except Exception as e:
            print("Error:", e)

        choice = input("\nSearch another city? (y/n): ").lower()

        if choice != "y":
            print("\nThank you for using Weather App!")
            break


if __name__ == "__main__":
    main()