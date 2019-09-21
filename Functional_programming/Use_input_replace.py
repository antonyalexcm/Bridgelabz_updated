
# User Input and Replace String Template “Hello <>, How are you?
name = input("Enter your Name: ")

#checking if name is atleast three digits.
if(len(name)<3): 
 print("Name too Small!!")
else:
 print("\nHello {}, How are you?".format(name))