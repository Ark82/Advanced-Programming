a = str(input("Enter your sentence to reverse:\n"))
for i in range(len(a)):
    print(a[len(a) - (i + 1)], end="")
