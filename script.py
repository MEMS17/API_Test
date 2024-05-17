# Essaie avec la récupération de code avec POSTMAN

# import requests

# url = "https://swapi.dev?id=5"

# payload = {}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

import requests
from flask import Flask

app = Flask(__name__)

@app.route("/bonjour")
def hello_world():
    return "Hello, World!"


@app.route("/bjr/<username>")
def name(username):
    return "Hello, "+ username

@app.route("/pokemon_test/<name>")
def verify_pokemon(name):
    pokemon_data = requests.get('https://pokeapi.co/api/v2/pokemon/'+ name)
    # json_recuperer = pokemon_data.json()  
    # pokemon_name = json_recuperer['name']
    # if pokemon_name == name:
    #     return "Pokemon existant"
    # else:
    #     return "Pokemon inexistant"
    
    try :
        json_recuperer = pokemon_data.json()
        pokemon_name = json_recuperer['name']
        return "Pokemon existant"
    except:
        return "Pokemon inexistant"

    
    # status_pokemon = pokemon_data.status_code
    # if status_pokemon == 200:
    #     return "Pokemon existant"
    # else :
    #     return "Pokemon inexistant"


@app.route("/find/<univers>/<id>")
def find(univers, id):
    if univers == "sw":
        sw_data = requests.get("https://swapi.dev/api/planets/"+id)
        json_recuperer_sw = sw_data.json() 
        return json_recuperer_sw 
        
    if univers == "pk":
        pokemon_data = requests.get("https://pokeapi.co/api/v2/pokemon/"+id)
        json_recuperer_pokemon = pokemon_data.json() 
        return json_recuperer_pokemon 
    else :
        return 'Univers non reconnu'    

app.run(debug = True)