# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("add number:" ))

for i in range(n):
    if 2**i <= n:
        print(2**i, end =" ")

# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1