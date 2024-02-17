import requests

while True:
    pokemon_name=input("Enter the Pokemon name: ")

    endpoint=f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    req=requests.get(endpoint)

    if req.status_code!=200:
        print("No data exists")
    else:
        poke_data = req.json()

        print(f"{pokemon_name} details are as follows:")

        print(f"Name: {poke_data['name']}")

        print("Abilities:")
        for ability in poke_data['abilities']:
            print(ability['ability']['name'])
    
    user_input=input("Do you want to look for another pokemon (Press y to continue..)?").lower()
    if user_input != 'y':
        print("Thank you for using the app. Exiting now...")
        break