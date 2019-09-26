Object Oriented Programs

1. JSON Inventory Data Management of Rice, Pulses and Wheats
  a.Desc -> Create a JSON file having Inventory Details for Rice, Pulses and Wheats with properties name, weight, price per kg. 
  b.Use Library : Java JSON Library, For IOS JSON Library use NSJSONSerialization for parsing the JSON.
  c.I/P -> read in JSON File
  d.Logic -> Get JSON Object in Java or NSDictionary in iOS. Create Inventory Object from JSON. Calculate the value for every Inventory. 
  e.O/P -> Create the JSON from Inventory Object and output the JSON String

2.Regular Expression Demonstration
  a.Desc -> Read in the following message: Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016. Use Regex to replace name, full name, Mobile#, and Date with proper value.
  b.I/P -> read in the Message
  c.Logic -> Use Regex to do the following
    i.Replace <<name>> by first name of the user ( assume you are the user)
    ii.replace <<full name>> by user full name.
    iii.replace any occurance of mobile number that should be in format 91-xxxxxxxxxx by your contact number.
    iv.replace any date in the format XX/XX/XXXX by current date.
  d.O/P -> Print the Modified Message.

3.Stock Report
  a.Desc -> Write a program to read in Stock Names, Number of Share, Share Price. Print a Stock Report with total value of each Stock and the total value of Stock.
  b.I/P -> N number of Stocks, for Each Stock Read In the Share Name, Number of Share, and Share Price
  c.Logic -> Calculate the value of each stock and the total value
  d.O/P -> Print the Stock Report.
  e.Hint -> Create Stock and Stock Portfolio Class holding the list of Stocks read from the input file. Have functions in the Class to calculate the value of each stock and the value of total stocks

4.Inventory Management Program
  a.Desc -> Extend the above program to Create InventoryManager to manage the Inventory. The Inventory Manager will use InventoryFactory to create Inventory Object from JSON. The InventoryManager will call each Inventory Object in its list to calculate the Inventory Price and then call the Inventory Object to return the JSON String. The main program will be with InventoryManager
  b.I/P -> read in JSON File
  c.Logic -> Get JSON Object in Java or NSDictionary in iOS. Create Inventory Object from JSON. Calculate the value for every Inventory. 
  d.O/P -> Create the JSON from Inventory Object and output the JSON String.
  
  

