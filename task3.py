# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# *Пример:*


n = int(input('Введите целое положительное число: '))
result = []

for i in range(1,n+1):
    result.append((1+1/i)**i)
print(result)

sum = 0
for i in range(n):
    sum = sum + result[i]
print(sum)