integer_list = [21,-34,17,-95,-43,69]

pos_list = []

for number in integer_list:
    if number > 0:
        pos_list.append(number)
        # Here you are saying if the number from the first list is a positive integer then you add it to the second, empty list (we represent this process using the .append() function)
print(pos_list)
    