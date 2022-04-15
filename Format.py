import json
manager_sales = {}
with open(r"manager_sales.json", "r", encoding="UTF-8") as file:
    data = json.load(file)
    str_json = json.dumps(data, indent=1)
    work = json.loads(str_json)
    for content in work:
        for key, value in content.items():
            name = ''
            worklist = 0
            if key == 'manager':
                for who in value.values():
                    name += who + ' '
            elif key == 'cars':
                for i in value:
                    worklist += i['price']
            manager_sales[name] = worklist


print(manager_sales)


