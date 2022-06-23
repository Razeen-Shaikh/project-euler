# initial fibonacci numbers a and b
a = 1
b = 1

n = 50000
sum = 0
for i in range(2, n):
    fib = a + b
    # making sure fibonacci number doesn't exceed 4 million
    if fib > 4000000:
        break
    # Checking if the fibonacci number is even
    if fib % 2 == 0:
        sum += fib
    a, b = b, fib

print(sum)
