import json

with open(r"manager_sales.json", "r", encoding="UTF-8") as file:
    data = json.load(file)
    str_json = json.dumps(data, indent=1)
    work = json.loads(str_json)
