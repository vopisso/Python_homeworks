import json

def write_json(dic):
    with open('F:/GB/Courses/Python1/Homeworks/HW7/json_storage.json', 'w', encoding='utf-8') as file:
            json.dump(dic, file, ensure_ascii=False, indent=4)

def read_json():
    with open('F:/GB/Courses/Python1/Homeworks/HW7/json_storage.json', encoding='utf-8') as f:
        temp_list = json.load(f)
        return temp_list
