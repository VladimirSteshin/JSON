import json

managers = {}
with open(r"manager_sales.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

for i in data:
    person = ''
    price = 0
    for name in i['manager'].values():
        person += name + ' '
        person.strip()
    for cost in i['cars']:
        price += cost['price']
    managers[person] = price

winner = max(managers.values())
for key, value in managers.items():
    if value == winner:
        print(f'{key}{value}')

