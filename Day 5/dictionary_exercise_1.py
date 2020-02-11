# Given the following dictionary, representing a mapping from names to phone numbers:

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
# Write code to do the following:

# Print Elizabeth's phone number.
# Add an entry to the dictionary: Kareem's number is 938-489-1234.
# Delete Alice's phone entry.
# Change Bob's phone number to '968-345-2345'.
# Print all the phone entries.

# 1
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth'])


#2
phonebook_dict['Kareem'] = '968-345-2345'

print(phonebook_dict)


#3
del phonebook_dict['Alice']

print(phonebook_dict)


#4 & #5 (technically)
phonebook_dict['Bob'] = '986-345-2345'

print(phonebook_dict)


