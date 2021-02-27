import math

#x = int(input('Vvedite X'))

def f12(x):

    if x < 50:
        sum = ((x ** 4) - math.sin(x))
#       print(sum)

    elif 50 <= x < 145:

        sum = ((abs(math.tan((math.e ** x) - (x ** 6)))) + math.e ** x)
#       print(sum)

    elif 145 <= x < 204:

        sum = ((x ** 8) + (x ** 6))
#       print(sum)

    else:

        sum = ((x ** 5) + abs(x) - 86)
    #print (sum)