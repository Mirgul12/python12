# # # set
# new_set = {9,2,3,4,5,6,1,8}
# print(new_set)
#
# set_ = {}
# print(type(set_))
# print(type(new_set))
# print(len(new_set))
# # # #
# # # Метод add() принимает один аргумент, который может быть любого типа,
# # # и добавляет данное значение в множество.
# #
# # # Метод update() принимает один аргумент — iterable, и добавляет все
# # # его элементы к исходному множеству
# #
# a_set = {1, 2, ('sad', 'all')}
# a_set.add(4)
# print(a_set)
# # a_set.add(('1','2','3'))
# print(a_set)
# list_ = (2,3,4,5,6,7,8,9,0,)
# b_set = {5,6,7,8}
# a_set.union(b_set)
# print(a_set)
# a_set.update(list_, ('1','2','3'))
# print(a_set)
# #
# # # method remove
# # a_set.remove(1)
# # print(a_set)
# #
# # # method discard
# # a_set.discard(2)
# # a_set.remove(0)
# # print(a_set)
# #
# # # method pop, Метод clear()
# # print(a_set.pop())
# # a_set.clear()
# # print(a_set)
# #
# # Метод union() (объединение) возвращает новое множество, складывает множества
#
# # a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
# # b_set = {1, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}
# # c_set = a_set.union(b_set)
# # print(a_set)
#
# # set_1 = {1,2,3,4,5,6,7,8,9}
# # set_2 = {2,4,6,8,222,333,444}
# # print(set_2.union(set_1))
#
# # Метод intersection() (пересечение) возвращает новое множество,
# # содержащее все элементы, которые есть и в первом множестве, и во
# # втором.
#
# set_1 = {1,2,3,4,5,6,7,8,9}
# set_2 = {2,4,6,8,222,333,444}
#
# # set_3 = set_1.intersection(set_2)
# # print(set_3)
#
# # Метод difference() (разность) возвращает новое множество, содержащее
# # все элементы, которые есть в множестве a_set, но которых нет в
# # множестве b_set.
#
# set_1 = {1,2,3,4,5,6,7,8,9}
# set_2 = {2,4,6,8,}
#
# print(set_1.union(set_2)) # сложение
# print(set_1.intersection(set_2)) # пересечение
# print(set_2.difference(set_1)) # разность
# print(set_1.symmetric_difference(set_2)) #симметричная разность
# #
# # Метод symmetric_difference() (симметрическая разность) возвращает
# # новое множество, которое содержит только уникальные элементы обоих
# # множеств.
#

# boolean

# x = 1
# y = 2
#
# if x < 0:
#     print(type(True))
# elif y < 0:
#     print(True)
# else:
#     print('сработал блок else')
# print('hello')


# ==  СРАВНЕНИЕ
# !=  Отрицание
# <  меньше
# > больше
# <= меньше равно
# >= больше равно
# and  и
# or  или
# not  не
# in  в
# point = input('Enter your point: ')
# if point == '5':
#     print('Молодец')
# elif point == "4":
#     print("Ты молодец, чуть чуть осталось до отличника")
# elif point == "3":
#     print("Старайся учиться лучше! ")
# else:
#     print("Ты можешь лучше учиться ")
#
# list_ = [1, 2, 3, 4, 5]
# num = int(input('enter a number: '))
#
# if num in list_:
#     print('есть такое число')
# else:
#     print('такого числа нет')
#
# if num not in list_:
#     print('такого числа нет')
# else:
# #     print('есть такое число')
# import math
#
# while True:
#     number1 = float(input('enter a number1: '))
#     number2 = float(input('enter a number2: '))
#     number3 = float(input('enter a number3: '))
#     operator = input('enter a operator +-/*: ')
#     if operator == '+':
#         if number1 == 1:
#             print('Ого ты ввел 1')
#         print(math.floor(number1 + number2 + number3))
#         print(round(number1 + number2 + number3))
#     elif operator == '-':
#         print(number1 - number2)
#     elif operator == '/':
#         print(number1 / number2)
#     elif operator == '*':
#         print(number1 * number2)
#     elif operator.isalpha():
#         print('вы остановили цикл')
#         break
#     else:
#         print('Введите оператор + - / *')





