import json

python_dict = {
    "name": "Om",
    "age": 21,
    "city": "Phuket"
}

json_string = json.dumps(python_dict)

print(json_string)