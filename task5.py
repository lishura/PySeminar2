# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Введите количество элементов списка: '))
result = []

for _ in range(n):
    result.append(random.randint(-10,10))
print(result)


for i in range(n):
    random_index = random.randint(0,n-1)
    temp = result[i]
    result[i] = result[random_index]
    result[random_index] = temp
print(result)