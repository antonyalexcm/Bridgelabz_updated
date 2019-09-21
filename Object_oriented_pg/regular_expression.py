import re
from datetime import date

# Function to carry out the mentioned regex operations
def regex_operation(string_read, user_details,today):
    string_read = re.sub(r"<<name>>",user_details[0],string_read)
    string_read = re.sub(r"<<full name>>",user_details[1],string_read)
    string_read = re.sub(r"(?<=\-)(.*?)(?=\.)",user_details[2],string_read)
    string_read = re.sub(r"(\d\d?)\/(\d\d??)\/(\d\d\d\d)",today.strftime("%d/%m/%Y"),string_read)
    print(string_read)

def main():
    string_read = str("""Hello <<name>>,
    We have your full name as <<full name>> in 
    our system. Your contact number is 91-xxxxxxxxxx.
    Please,let us know in case of any clarification
    Thank you BridgeLabz 01/01/2016.""")
    today = date.today()
    user_details = ['Antony','Antony Alex', '9567445279']
    regex_operation(string_read, user_details, today) 


# Driver Function
if __name__ == "__main__":
    main()

    
    
    
