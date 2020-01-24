N = int(input("Please select a number value N: "))

side = int(N)

while side <= N:
    for i in range(side):
        for i in range(side):
            print("*", end= " ")
        print()
    break
