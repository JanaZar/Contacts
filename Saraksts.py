contacts = []

while(True):
    print('Enter your choice,\n1 - add new contact;\n2 - Show contact;\n3 - Exit; (1/2/3?) ')
    i = input('Your choice: ')
    if i == '1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_age = input('Age: ')
        person_phone = input('Phone: ')
        person_email = input('Email: ')

        person_contact = {
            'name': person_name,
            'surname': person_surname,
            'age': person_age,
            'phone': person_phone,
            'email': person_email
    }

        contacts.append(person_contact)

    elif i == '2':
       print('Show list?')
       n = input('y/n?: ')
       if n == 'y':
        for i in contacts:
            print('====CONTACTS====')
            print(f"{i['name']} {i['surname']}")
            print(f"Age: {i['age']}")
            print(f"Phone: {i['phone']}")
            print(f"Email: {i['email']}")
        
        

    elif i == '3': 
        print('Bye bye <3')
        exit()
    
    else:
        print('Please choose 1;2;3?')
