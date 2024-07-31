# print a table using reversed order
num = int(input("Enter a number: "))
i = 1

for i in range (10,0,-1):
    print(f"{num}X{i}={i*num}")

print("done")    
