# 1.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint

# n = int(input('Введите размер списка '))
# lst = []
# lst_2 = []

# for i in range(n):
#     lst.append(randint(-10, 10))

# for i in range(len(lst)):
#     while i < len(lst)/2 and n > len(lst)/2:
#         n = n - 1 
#         a = lst[i] * lst[n]
#         lst_2.append(a)
#         i += 1

# print(lst)
# print(lst_2)




# 2.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import uniform


# n = int(input('Введите размер списка '))
# lst = []
# for i in range(n):
#     f = uniform(0, 9)
#     lst.append(round(f, 2))

# lst_2 = [round(i%1,2) for i in lst if i%1 != 0]

# print(lst)
# print(lst_2)
# print(max(lst_2) - min(lst_2))





# 3.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# n = int(input("Введите число: "))
# x = ""
# while n > 0:
#     x = str(n % 2) + x
#     n = n // 2
# print(x)

# n = int(input("Введите число: "))
# print(bin(n))
# print(bin(n)[2:])