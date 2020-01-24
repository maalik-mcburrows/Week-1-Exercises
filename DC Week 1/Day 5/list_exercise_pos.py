integer_list = [21,-34,17,-95,43,69]

for number in integer_list:
    if number > 0:
    # Note how you defined number(which is an int value) first as a representation of individual entries in the list integer_list, then compared that value number with an actual integer. Comparing it to a string, list, etc. would not work.
        print(number)

