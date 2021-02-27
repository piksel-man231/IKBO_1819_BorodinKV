import math

n = int(input())

f_1 = 10
for i in range (0, n):
#   f = ((1 / 53) * f_1 + math.cos(f_1) - 60)
    f1 = 1/53 * f_1
    f2 = math.cos(f_1)
    f = f1 + f2 - 60
    f_1 = f

print(f_1)
