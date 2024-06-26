size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    for x in range(size):
        print("*", end="")
    print("\n")
    row = row + 1
