
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


contact = {}
cond = True
while cond:
    choice = int(input("1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 5. Delete Contact \n Enter your choice:"))
    if choice == 1:
        name = input("enter the contact name: ")
        phone = input("enter the mobile number: ")
        contact[name] = phone
    elif choice == 2:
        search_name = input("enter the contact name: ")
        if  search_name in contact:
            print(search_name, "'s contact number is ", contact[search_name])
        else:
            print("Name is not in the phonebook")
    elif choice == 3:
        if not contact:
            print("empty phonebook")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the name to be edited: ")
        if edit_contact in contact:
            phone = input("Enter the mobile number: ")
            contact[edit_contact] = phone
            print("contact updated")
            display_contact()
        else:
            print("Name is not found in the phonebook")
    elif choice == 5:
        del_contact = input("enter the contact to be deleted: ")
        if del_contact in contact:
            answer = input("Do you want to delete the contact yes or no? ")
            if confirm == "yes":
                contact.pop(del_contact)
            display_contact()
        else:
            print("name is not found in the phonebook")
    else:
        condition = input("Do you want to exit? y/n ")
        if condition == 'y' or condition == 'Y':
            print("Goodbye!")
            cond = False

