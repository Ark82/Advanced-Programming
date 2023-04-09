def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


x = int(input("Enter your number: "))
if is_prime(x):
    print("Your number is a prime number!")
else:
    print("Your number is not a prime number!")
