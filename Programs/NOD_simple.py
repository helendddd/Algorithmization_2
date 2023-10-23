a = int(input("\nВведите a... "))
b = int(input("Введите b... "))

nod = 1

for i in range (2, min(a,b)):
    if a % i == 0 and b % i == 0:
        nod = i
        
print (nod)
