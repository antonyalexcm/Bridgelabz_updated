import json

# Save a python dict object to JSON format file.
def python_dict_to_json_file(file_path):
    try:
        # Get a file object with write permission.
        file_object = open("./Inventory_data_final.json", 'w')

        # Save dict data into the JSON file.
        json.dump(dict_object, file_object)

        print(file_path + " created. ")    
    except FileNotFoundError:
        print(file_path + " not found. ")    

if __name__ == '__main__':
    python_dict_to_json_file("./teacher_data.json")