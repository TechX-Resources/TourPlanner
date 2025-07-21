import requests

class Travel_info():

    def __init__(self, name, base_url, api_key=None):
        self.name = name
        self.base_url = base_url
        self._api_key = api_key
    

class Hotel(Travel_info):
    def __init__(self, name, base_url, api_key=None):
        super().__init__(name, base_url, api_key)
        self.info = {}

    def get_hotel_list(self, url: str, params: dict):
        url = url
        headers = {"accept": "application/json",
                   "X-API-Key": self._api_key,
                   }
        response = requests.get(url, headers=headers, params=params)
        return response

    def get_hotel(self, url, params_list, city_list):
        hotel_list = {}
        index = 0
        for params in params_list:
            response = self.get_hotel_list(url, params)
            hotel_list[city_list[index]] = response.json()["data"]
            index += 1
        return hotel_list


        
