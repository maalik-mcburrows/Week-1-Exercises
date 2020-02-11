x = 1

while x < 11:
    for i in range (1, 11):
        for j in range (1, 11):
            print("%d x %d =" % (i,j), i * j, end= "   ")
            # print(" ", end= " ")
        print("  ")

        x += 1
    