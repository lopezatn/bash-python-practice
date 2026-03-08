import json

with open("config.json") as f:
    data = json.load(f)

for key, value in data.items():
    print(f"{key}: {value}")
