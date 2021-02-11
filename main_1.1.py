import math

num_1 = int(input('Vvedite X'))
num_2 = int(input('Vvedite Y'))
#Perviy kusok

sum_1 = math.sqrt((num_1 ** 4) - abs(num_1))

#Vtoroy kusok

presum2_top = (abs(num_2) + math.tan(num_1))
presum2_bot = ((math.e ** num_2) - (num_1 ** 6))

sum_2 = presum2_top / presum2_bot

#Tretiy kusok

presum3_top = ((num_2 ** 5) + (25 * (num_1 ** 8)))
presum3_bot = ((31 * (num_2 ** 6)) + (36 * (num_2 ** 4)))
sum_3 = math.sqrt(presum3_top / presum3_bot)

#Final calculation

print(sum_1 - sum_2 + sum_3)