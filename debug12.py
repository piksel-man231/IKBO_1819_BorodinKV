import math

x = int(input())

if x < 50:
    sum1 = ((x ** 4) - math.sin(x))
    print(sum1)

elif 50 <= x < 145:
    sum1 = ((abs(math.tan((math.e ** x) - (x ** 6)))) + math.e ** x)
    print(sum1)

elif 145 <= x < 204:
    sum1 = ((x ** 8) + (x ** 6))
    print(sum1)

else:
    sum1 = ((x ** 5) + abs(x) - 86)
    print(sum1)
