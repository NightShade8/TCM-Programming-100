#Dictionaries - key/value pairs {}

drinks = {"White Russian": 8, "Old Fashioned": 12, "Lemon Drop": 5} #drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)
employees['Legal'] = ["Mr. Frond"] #add a new key/value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #add a new key/value pair
print(employees)

drinks['White Russian'] = 9
print(drinks)

print(drinks.get("White Russian"))