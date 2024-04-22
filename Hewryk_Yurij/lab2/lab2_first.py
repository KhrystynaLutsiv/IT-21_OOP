person = {
    "name": "Юра",
    "age": 18,
    "city": "Дубляни"
}

name = person["name"]
age = person["age"]

for value in person.values():
    print(value)

person["job"] = "програміст"

person["age"] = 31

del person["job"]

person.clear()
