import requests
import random

def handle(req):
    r = requests.get("http://api.open-notify.org/astros.json")
    result = r.json()
    
    index = random.randint(0, len(result["activities"])-1)
    name = result["activities"][index]["name"]
    desc = result["activities"][index]["desc"]
    url = result["activities"][index]["URL"]

    return "%s for startups \\n %s \\n \\n Know more @ %s" % (name) %desc %url
