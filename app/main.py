import json
from llm import LLM
import tools
from travel_api import Hotel
from dotenv import load_dotenv
import os
from utils import process_hotel_query_params
import utils

load_dotenv()




if __name__ == "__main__":

    load_dotenv(dotenv_path="api_keys.env")

    llm = LLM("open-api-key", "llm-tourplanner")
    llm.get_api_key()
    llm.setup()
    
    validity = False
    #user input schema
    input_schema = "schemas/user_input_test.schema.json"
    #user input string
    user_input = ""

    while (validity == False):
        #for testing user input
        user_input = user_input + input("input your travel plan and preference: ")
        #call for validation
        validity, data = tools.validate_user_input(llm.llm, input_schema, user_input)
        if(validity == False):
            print(data)

    print("user input valid")
    
    hotel_params, city_list = process_hotel_query_params(data)

    hotel = Hotel("hotel","https://api.liteapi.travel", os.getenv("LITEAPI_KEY"))
    hotel_list = hotel.get_hotel("https://api.liteapi.travel/v3.0/data/hotels", hotel_params, city_list)

    output = tools.generate_plan(llm.llm, user_input, data, hotel_list)
    print(output)

    







