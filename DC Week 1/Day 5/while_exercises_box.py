N = int(input("Please select a number value for height: "))
M = int(input("Please select a number value for width: "))

side = N
# Ask about side = N in class, not sure why it works

while side <= N:
    for i in range(0, N + 1):
        for j in range(0, M + 1):
            if(i == 0 or j == 0 or i == N or j == M):
                print("*", end= " ")
            else:
                print(" ", end= " ")
        print()
    break
