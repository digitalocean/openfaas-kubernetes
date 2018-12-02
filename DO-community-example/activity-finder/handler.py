import requests
import random

def handle(req):
    r = requests.get("https://openfaas-demo.sgp1.digitaloceanspaces.com/activities.json")
    result = r.json()
    
    index = random.randint(0, len(result["activities"])-1)
    name = result["activities"][index]["name"]
    desc = result["activities"][index]["desc"]
    url = result["activities"][index]["url"]

    return "%s for startups \\n %s \\n \\n Know more @ %s" % (name) %desc %url
