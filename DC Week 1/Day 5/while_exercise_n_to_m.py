n = int(input("Please select a number to begin from "))
m = int(input("Please select a number to end at "))
# Because we will need to iterate through the two inputs and increase the first input in consecutive instances (using n += 1) we need to set the two functions as integers.

while n <= m:
    print(n)
    n += 1

# if n != int:
#     print(input("Please choose a valid number"))
    