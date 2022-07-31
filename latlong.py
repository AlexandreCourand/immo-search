# Import the required library
from geopy.geocoders import Nominatim

def latlong(town):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="immo-search")

    location = geolocator.geocode(town)

    #print("The latitude of the location is: ", location.latitude)
    #print("The longitude of the location is: ", location.longitude)
    
    return {
        "long" : location.longitude,
        "lat" : location.latitude
    }