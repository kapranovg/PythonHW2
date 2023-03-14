"""На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.

5 -> 1 0 1 1 0
2"""

from random import randint

n = int(input("Введите число монет: "))

result = [randint(0, 1) for _ in range(n)]

print(result)

count0 = 0
count1 = 0

index = 0

while index < len(result):
    if result[index] == 0:
        count0 += 1
    elif result[index] == 1:
        count1 += 1
    index += 1


if count0 < count1:
    print(count0)
else:
    print(count1)