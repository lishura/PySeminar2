# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random
n = int(input('Введите целое положительное число: '))
result = []

for i in range(1, n+1):
    result = [random.randint(-n, n) for i in range(n)]
    # result.append(random.randint(-n,n))
print(result)
data = open('file.txt', 'r')
mult1 = int(data.readline())
mult2 = int(data.readline())
if mult1 < n and mult2 < n:
    product = result[mult1]*result[mult2]
    print(product)
else:
    print("Позиции из файла отсутствуют в списке")
