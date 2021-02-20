import json

json_string = '{"name": "Om", "age":21, "city": "Phuket"}'

python_dict = json.loads(json_string)

print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])