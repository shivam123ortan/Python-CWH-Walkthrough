a = int(input("Enter a number: "))
i = 1

while i <= a:
    i = i + 1
    print("Sum of first " + str(a) + " integers is: " + str((a/2)*(2+(a-1))))
    break
print("Done")    