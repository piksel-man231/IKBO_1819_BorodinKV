import math

n = int(input('Vvedite N'))

f_1 = 10
for i in range (1, n+1):
    f = (((1/53) * f_1 + math.cos(f_1)) - 60)
    f_1 = f

print (f-1)