fib1 = 1
fib2 = 1

n = int(input("\nВведите n... "))

for i in range (2,n):
    fib = fib1+fib2
    fib1 = fib2
    fib2 = fib

print (fib2)