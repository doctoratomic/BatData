from email.utils import parseaddr
import json
from re import search
filename = "./data/villains.json"

def Choices():
    batlogo = ("""_____________________                              _____________________
    `-._:  .:'   `:::  .:\           |\__/|           /::  .:'   `:::  .:.-'
    \      :          \          |:   |          /         :       /    
     \     ::    .     `-_______/ ::   \_______-'   .      ::   . /      
      |  :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: :|       
      |     ;::         ;::         ;::         ;::         ;::  |       
      |  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:|       
      /     :           :           :           :           :    \       
     /______::_____     ::    .     ::    .     ::   _____._::____\      
                   `----._:: ::'  :   :: ::'  _.----'                    
                          `--.       ;::  .--'                           
                              `-. .:'  .-'                               
                                 \    /                             
                                  \  /                                   
                                   \/ """)
    print(batlogo)
    print(""" ________  ________  _________  ________  ________  _________  ________  ________  ________  ________  _______      
|\   __  \|\   __  \|\___   ___\\   ___ \|\   __  \|\___   ___\\   __  \|\   __  \|\   __  \|\   ____\|\  ___ \     
\ \  \|\ /\ \  \|\  \|___ \  \_\ \  \_|\ \ \  \|\  \|___ \  \_\ \  \|\  \ \  \|\ /\ \  \|\  \ \  \___|\ \   __/|    
 \ \   __  \ \   __  \   \ \  \ \ \  \ \\ \ \   __  \   \ \  \ \ \   __  \ \   __  \ \   __  \ \_____  \ \  \_|/__  
  \ \  \|\  \ \  \ \  \   \ \  \ \ \  \_\\ \ \  \ \  \   \ \  \ \ \  \ \  \ \  \|\  \ \  \ \  \|____|\  \ \  \_|\ \ 
   \ \_______\ \__\ \__\   \ \__\ \ \_______\ \__\ \__\   \ \__\ \ \__\ \__\ \_______\ \__\ \__\____\_\  \ \_______\
    \|_______|\|__|\|__|    \|__|  \|_______|\|__|\|__|    \|__|  \|__|\|__|\|_______|\|__|\|__|\_________\|_______|
                                                                                               \|_________|         """)
    print("(1) View Data")
    print("(2) Search Data")
    print("(3) Add Data")
    print("(4) Delete Data")
    print("(5) Edit Data")
    print("(6) Exit")
    
database = filename
data = json.loads(open(database).read())
    
def view_data():
    with open (filename, "r") as f:
        temp = json.load(f)
        i = 0
        for entry in temp:
            name = entry["name"]
            alias = entry["alias"]
            birthday = entry["birthday"]
            nemesis = entry["nemesis"]
            powers = entry["powers"]
            print(f"Index Number {i}")
            print(f"Real Name:  {name}")
            print(f"Codename:  {alias}")
            print(f"Date of Birth:  {birthday}")
            print(f"Nemesis:  {nemesis}")
            print(f"Powers:  {powers}")
            print("\n\n")
            i=i+1

def delete_data():
    view_data()
    new_data = []
    with open (filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print("Which number would you like to remove?: ")
    delete_option = input(f"Select a number 0-{data_length}: ")
    i=0
    for entry in temp:
        if i == int(delete_option):
            pass
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
    with open (filename, "w") as f:
        json.dump(new_data, f, indent=4)
    

def edit_data():
    view_data()
    new_data = []
    with open(filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print("Which index number would you like to delete?")
    edit_option = input(f"Select a number 0-{data_length}")
    i=0
    for entry in temp:
        if i == int(edit_option):
            name = entry["name"]
            alias = entry["alias"]
            birthday = entry["birthday"]
            nemesis = entry["nemesis"]
            powers = entry["powers"]
            print(f"Current Real Name:  {name}")
            name = input("Update?: ")
            print(f"Current Codename:  {alias}")
            alias = input("Update?: ")
            print(f"Current Date of Birth:  {birthday}")
            birthday = input("Update?: ")
            print(f"Current Nemesis:  {nemesis}")
            nemesis = input("Update?: ")
            print(f"Current Powers:  {powers}")
            powers = input("Update?: ")
            new_data.append({"name": name, "alias": alias, "birthday": birthday, "nemesis": nemesis, "powers": powers})
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
    with open (filename, "w") as f:
        json.dump(new_data, f, indent=4)
            

def add_data():
    item_data = {}
    with open (filename, "r") as f:
        temp = json.load(f)
    item_data["name"] = input("Real Name: ")
    item_data["alias"] = input("Codename: ")
    item_data["birthday"] = input("Date of Birth: ")
    item_data["nemesis"] = input("Nemesis: ")
    item_data["powers"] = input("Powers: ")
    temp.append(item_data)
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
while True:
    Choices()
    choice = input("\nEnter Number: ")
    if choice == "1":
        view_data()
    elif choice == "2":
        print("This feature hasn't been added yet...")
    elif choice == "3":
        add_data()
    elif choice == "4":
        delete_data()
    elif choice == "5":
        edit_data()
    elif choice == "6":
        break
    else:
        print("Please pick a number...")