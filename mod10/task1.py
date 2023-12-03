import json
import requests

response = requests.get("https://swapi.dev/api/starships/10/")
data = json.loads(response.text)
falcon_info = {
"name": data['name'],
"max_atmosphering_speed": data['max_atmosphering_speed'],
"starship_class": data['starship_class'],
"pilots": []
}

pilots_url = data["pilots"]
for pilot_url in pilots_url:
    response = requests.get(pilot_url)
    pilot = json.loads(response.text)
    response = requests.get(pilot['homeworld'])
    homeworld = json.loads(response.text)
    pilot_info ={
        "name": pilot['name'],
        "height": pilot['height'],
        "mass": pilot['mass'],
        "homeworld": homeworld['name'],
        "homeworld_url": pilot['homeworld']
    }

    
    falcon_info["pilots"].append(pilot_info)
    

with open("my_test.json", "w") as file:
    json.dump(falcon_info, file, indent=4)
