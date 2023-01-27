result = requests.get(f"https://meowfacts.herokuapp.com/?count=1").json()
for data in result.values():
    for elements in data:
        elements
    
