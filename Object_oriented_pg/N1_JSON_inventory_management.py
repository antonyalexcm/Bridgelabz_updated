 
# @author:Antony Alex
# @version:3.7
# @purpose:Reading a file from json

#importing necessary libraries
import json

def inventory_management():
    #Function to read the .json file and carryout the necessary operations
    with open('Inventory_pulses.json') as f:
        data = json.load(f)
    print("\n")
    
    new_inven = {} 
    
    for inventory in data['Inventories']:
        intermediate = str(inventory['weight_in_kg']*inventory['price_per_kg'])
        new_inven[inventory['name']] = "Rs."+intermediate   
    
    json_final = json.dumps(new_inven, indent = 2)
    print(json_final)

def main():
    inventory_management()
    
#Driver Function
if __name__ =="__main__":
    main()