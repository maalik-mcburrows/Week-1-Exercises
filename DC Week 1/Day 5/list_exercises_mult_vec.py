num_list = [2,7,4]
other_num_list = [3,9,5]

new_list = [num_list * other_num_list for num_list,other_num_list in zip(num_list,other_num_list)]
# The zip() function returns an iterator of tuples(a finite ordered sequence of elements) where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc. In this case we have to specify using the [] that we want to perform multiplication (num_list * other_num_list) between the two lists (for num_list,other_num_list) in the zip() fxn (in zip(num_list,other_num_list))
print(new_list)

