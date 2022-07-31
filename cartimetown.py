import requests
import json
import datetime

def getTime():
    # call the OSMR API
    r = requests.get(f"http://router.project-osrm.org/route/v1/car/3.0778827,50.6056749;3.1763889,49.22361?overview=false""")
    # then you load the response using the json libray
    # by default you get only one alternative so you access 0-th element of the `routes`
    routes = json.loads(r.content)
    route_1 = routes.get("routes")[0]
    print(str(datetime.timedelta(seconds=route_1["duration"])))