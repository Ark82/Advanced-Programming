def fibo(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)


num = int(input("Enter your number: "))
print(f"The nth number of Fibonacci sequence is: {fibo(num)}")
