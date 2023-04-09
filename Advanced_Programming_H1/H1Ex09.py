def is_prime(x):
    for i in range(2,x):
        if x % i == 0 and x != 1:
            return False
    return True


def prime_str(x):
    a = ""
    for i in range(len(x)):
        if is_prime(i):
            a += x[i]
    return a


a = str(input("Enter your sentence: "))
print(prime_str(a))
