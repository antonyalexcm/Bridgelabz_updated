import json

class Inventory:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

class Inventory_manager:
    def __init__(self):
        self.inventory_list = []

    def create_list_append(self):
        invent_dict = read_file()
        for inventory in invent_dict['Inventories']:
            invent_obj = object(inventory['name'],inventory['weight_in_kg'],inventory['price_per_kg'])
            #invent_obj = Inventory(inventory['name'],inventory['weight_in_kg'],inventory['price_per_kg'])
            self.inventory_list.append(invent_obj)
    
    def print_value(self):
        print("\rThe value of various inventories is : ")
        for inventory in self.inventory_list:
            print("\r{} = Rs.{}".format(inventory.name,inventory.weight*inventory.price))
        dicti = {"Inventories" : []}
        for inventory in self.inventory_list:
            dictionary = {"name": inventory.name ,"weight_in_kg": inventory.weight,"price_per_kg": inventory.price}
            dicti["Inventories"].append(dictionary)
        json_final = json.dumps(dicti, indent=2)
        create_new_file(json_final)



def read_file():
    with open('Inventory_pulses.json') as f:
        data = json.load(f)
    return data 

def create_new_file(file_json):
      try:
        # Get a file object with write permission.
        file_object = open("./Inventory_data_final.json", 'w')
        # Save dict data into the JSON file.
        json.dump(file_json, file_object,indent=2)

        print("File created. ")   

      except FileNotFoundError:
            print("File not found. ")
    

def main():
    inventor = Inventory_manager()
    inventor.create_list_append()
    inventor.print_value()


if __name__ == "__main__":
    main()
   
    
