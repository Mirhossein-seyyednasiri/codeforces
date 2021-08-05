data = input().split(" ")
n = int(data[0])
m = int(data[1])
a = int(data[2])




if n % a == 0 :
    k1 = n // a
else:
    k1 = n//a + 1

if m % a == 0 :
    k2 = m // a 
else:
    k2 = m // a + 1


print(k1 * k2)