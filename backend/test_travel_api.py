from travel_api import Weather_WeatherAPI  # ✅ new weather class
from travel_api import (Directions_OpenRouteService,
                        FutureFlight_Aviationstack, Hotel_LiteAPI,
                        Hotel_RapidAPI)

hotel_rapid = Hotel_RapidAPI("Hotel Rapid API")
hotel_lite = Hotel_LiteAPI("Hotel Lite API", "https://api.liteapi.travel")
weather_api = Weather_WeatherAPI("WeatherAPI Forecast")  # ✅ updated instance
direction = Directions_OpenRouteService("Directions (OpenRouteService)")
future_flight = FutureFlight_Aviationstack("Future Flight Schedules (Aviationstack)")

def test_travel_apis():
    print("\n--- Testing Hotel Search ---")
    params_hotel = {
        "city": "Paris",
        "countryCode": "FR",
        "minRating": 8,
        "starRating": 4,
        "limit": 3,
        "aiSearch": "Hotels near Eiffel tower"
    }
    hotels = hotel_lite.get_hotel_list(url="https://api.liteapi.travel/v3.0/data/hotels", params=params_hotel)
    if hotels:
        print(hotels)
    else:
        print("No hotel data returned.")

    print("\n--- Future Weather Forecast by City ---")
    weather_params_city = {
        "city": "Paris",
        "date": "2025-08-02"
    }
    forecast_city = weather_api.get_forecast(weather_params_city)
    print(forecast_city)

    print("\n--- Future Weather Forecast by Coordinates ---")
    weather_params_coords = {
        "lat": 48.8566,
        "lon": 2.3522,
        "date": "2025-08-02"
    }
    forecast_coords = weather_api.get_forecast(weather_params_coords)
    print(forecast_coords)

    print("\n--- Testing Directions ---")
    params_direction = {
        "start_lon": 2.3522,
        "start_lat": 48.8566,
        "end_lon": 2.295,
        "end_lat": 48.8738
    }
    directions = direction.get_directions(params_direction)
    if directions:
        print(f"Route summary: {directions.get('routes', [{}])[0].get('summary', {})}")
    else:
        print("No directions data returned.")

    print("\n--- Testing Future Flight Schedules ---")
    params_flight = {
        "airport_dep": "LAX",
        "airport_arr": "SCL",
        "date_dep": "2025-09-01",
        "date_arr": "2025-09-01"
    }
    flights = future_flight.get_future_flight_schedules(params_flight)
    if flights:
        print(f"Found {len(flights)} flights departing from LAX on 2025-09-01")
        first_flight = flights[0]
        print(f"First flight info:\n Airline: {first_flight.get('airline', {}).get('name')}\n"
              f"Flight Number: {first_flight.get('flight', {}).get('iataNumber')}\n"
              f"Departure Time: {first_flight.get('departure', {}).get('scheduledTime')}")
    else:
        print("No flight schedule data returned.")

if __name__ == "__main__":
    test_travel_apis()
