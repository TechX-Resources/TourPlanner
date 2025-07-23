


def process_hotel_query_params(parsed_input, limit = 4, aiSearch = None):
    """
    This f unction is for proces hotel info from Liteapi travel

    Args:
        parsed_input: parsed user input
        limit: number of hotel fetch for each city
        aiSearch: additional requirement on hotel, such as hotel near shopping center

    Return:
        parameters for api call to fetch hotel information and a list of city
    """
    #for each city traveled to, generate query to fetch hotel
    days = parsed_input["daily_plan"]
    list_params = []
    city_list = [] 

    for day in days:
        param = {}
        param["countryCode"] = day["country_code"]
        param["cityName"] = day["city"]
        if day["accomondation"]["hotel_name"] != "":
            param["hotelName"] = day["accomondation"]["hotel_name"]
        param["starRatingparam"] = day["accomondation"]["hotel_rating"]
        param["limit"] = limit
        if aiSearch != None:
            param["aiSearch"] = aiSearch
        list_params.append(param)
        city_list.append(day["city"])
    return list_params, city_list
