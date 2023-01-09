import json

file = open('contacts.json', 'r', encoding='utf-8')
dictionary = json.load(file)
contacts = dictionary['contacts']
file.close() 

while(True):
    print('Enter your choice,\n1 - add new contact;\n2 - Show contact;\n3 - Exit; (1/2/3?) ')
    i = input('Your choice: ')
    if i == '1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_age = input('Age: ')
        person_phone = input('Phone: ')

        person_contact = {
            'name': person_name,
            'surname': person_surname,
            'age': person_age,
            'phone': person_phone,
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
        
        

    elif i == '3': 
        dictionary = {'contacts' : contacts}
        file = open('contacts.json', 'w', encoding='utf-8')
        json.dump(dictionary, file, indent = 4)
        file.close()
        print('Data saved! -^.^-')
        print('Bye bye <3')
        exit()
    
    else:
        print('Please choose 1;2;3?')
