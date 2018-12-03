import requests
import random

def handle(req):
    #r = requests.get("https://openfaas-demo.sgp1.digitaloceanspaces.com/activities.json")
    r = requests.get("https://openfaas-demo.sgp1.cdn.digitaloceanspaces.com/activities.json")
    result = r.json()
    
    index = random.randint(0, len(result["activities"])-1)
    name = result["activities"][index]["name"]
    desc = result["activities"][index]["desc"]
    url = result["activities"][index]["url"]

    return "%s for startups \n \n %s  \n \n For more details, see - %s" % (name,desc,url)
