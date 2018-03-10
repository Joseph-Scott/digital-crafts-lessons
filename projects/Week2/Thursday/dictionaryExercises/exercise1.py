phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}
# Step 1
print phonebook_dict['Elizabeth']

#step 2
phonebook_dict['Kareem'] = '404-123-1234'
print phonebook_dict['Kareem']

#step 3 - Delete Alice
del phonebook_dict['Alice']
print phonebook_dict

#step 4 - Change Bob's phone number
phonebook_dict['Bob'] = '404-444-4444'
print phonebook_dict['Bob']

#step 5 - print the dictionary
print phonebook_dict