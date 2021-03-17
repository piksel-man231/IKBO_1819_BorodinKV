import math

#   n = int(input('Vvedite N'))
#   m = int(input('Vvedite M'))
#   sum_1 = 0
#   sum_2 = 0


def f13(n, m, sum_1, sum_2):

    for i in range(1, n+1):
        sum_1 = (sum_1 + ((i ** 4) - abs(i)))

    for i in range(1, n+1):
        for j in range(1, m+1):
         sum_2 = (sum_2 + (math.log(j)) + (i ** 4))

    sum_3 = sum_1 + 42 * sum_2
    # print(sum_1 + 42 * sum_2)
    return sum_3
