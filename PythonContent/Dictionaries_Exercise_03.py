if __name__ == "__main__":
    cities = {
        "Kastoria": {
            "country":"Greece",
            "population":13000,
            "fact":"Kastoria has a lake",
        },
        "Thessaloniki": {
            "country":"Greece",
            "population":300000,
            "fact":"Thessaloniki is the second biggest city in greece",
        },
        "Kozani": {
            "country":"Greece",
            "population":500000,
            "fact":"Kozani is a city in northern Greece",
        },

    }

    for city, cityInfo in cities.items():
        print(f'{city}   {cityInfo["country"]}    {cityInfo["population"]}    {cityInfo["fact"]}')