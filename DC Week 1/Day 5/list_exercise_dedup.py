first_list = [1,2,3,1,4,5]

first_list = list(dict.fromkeys(first_list))
# for this problem you have to convert the list into a dictionary because dictionaries cannot contain repeats, we do this using the dict.() function). Once Python reads this inside the parenthesis it will then go on to the outside part (list()) which converts the dictionary back into a list. 

print(first_list)