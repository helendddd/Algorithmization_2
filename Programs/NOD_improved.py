def EUCLIDgcd(m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if m >= n:
        return EUCLIDgcd(m % n, n)
    if n >= m:
        return EUCLIDgcd(m, n % m)
 
a = int(input("\nВведите a... "))
b = int(input("Введите b... "))

print(EUCLIDgcd(a, b))