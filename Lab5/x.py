import json

DATA_FILE = "data_tmp.json"
with open(DATA_FILE, 'r', encoding='utf-8') as data_file:
    data_json = json.load(data_file)