# new_list = []
# empty_list = list()
# list_ = [1, 2, 3, 4, 5, 6]
# print(list_)
# print(len(list_))
#
# diapazon = range(1, 21)
# print(list(range(1, 21)))

# method append добавляет элементы в конец списка
# some_list = [1, 2, 3, 4, 5]
# print(some_list)
# some_list.append(6)
# print(some_list)
# some_list.append('python')
# print(some_list)
# print(len(some_list))
# new_list = [1,2,3]
# some_list.append(new_list)
# print(some_list)
# print(len(some_list))

# method extend расширяет список, другим списком
#
# list1 = ['user1', 'user2', 'user3']
# list2 = ['Erkin', 'Kirill', 'Aika']
# list1 = list1 + list2
# # list1 += list2
# list1.extend(list2)
#
# print(list1)
# print(list1)
#
# # method insert получает 2 аргумента и добавляет в список поиндексно
#
# cars = ['Mersedes', 'Honda', 'Subaru']
# print(cars)
# cars.insert(0, 'Toyota')
# print(cars)


# method remove удалаляет элемент по значению
#
# laptops = ['Lenovo', 'Macbook', 'Acer', 'Asus', 'Hp']
# laptops.remove('Asus')
# print(laptops)

# method pop удаляет по умолчанию последний элемент, но можно передать индекс удаляемого элемента

# laptops = ['Lenovo', 'Macbook', 'Acer', 'Asus', 'Hp']
# notebook = laptops.pop(1)
# last_notebook = laptops.pop()
# print(laptops)
# print(notebook)
# print(last_notebook)


 # method index возвращает индекс элемента
#
# laptops = ['Lenovo', 'Macbook', 'Acer', 'Asus', 'Hp']
# print(laptops.index('Asus'))

# method count
# #
# numbers = [1, 2, 3, 4, 1, 2, 3, 1, 1, 1, 2, 2]
# print(numbers.count(2))


# method reverse разворачивает список
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers.reverse()
# print(numbers)

# method sort сортирует по ключу
#
# nums = [1, 5, 9, 2, 3, 8, 4]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# laptops = ['Lenovo', 'Macbook_Pro', 'Acer', 'Asus', 'Hp']
# laptops.sort(key=len)
# print(laptops)
#


# method copy
# cars = ['honda', 'Audi', 'Mercedes', ['hello', 'world']]
# print(cars)
# new_cars = cars.copy()
# new_cars[3][0] = 'BMW'
# print(new_cars)
# print(cars)
# numbers = [1, 2, 3, 4, 5, [6, 7, 8, 9]]
# numbers_2 = numbers.copy()
# numbers_2[5][0] = "шесть"
# print(numbers)
# print(numbers_2)

# method deepcopy
# import copy
# list_ = [1, 2, 3, [4, 5, 6]]
# print('Original', list_)
# new_list = copy.deepcopy(list_)
# print('Copy', new_list)
# new_list[3][0] = 'Changed'
# print('copy', new_list)
# print('Original', list_)

# method clear - полностью очищает список
# method del удаляет элемент по индексу
# cars = ['honda', 'Audi', 'Mercedes', ['hello', 'world']]
# # cars.clear()
# del cars[1]
# print(cars)
# cars.clear()
# print(cars)


# Срезы
#
# list_ = [1,2,3,4,5,6,7,8,9]
# print(list_[0:5])
# print(list_[1::2])

# Кортежи - tuples

# new_tuple = ('abc',)
# print(type(new_tuple))
# tuple_ = tuple()
# print(type(tuple_))
# print(dir(tuple_))
#
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, (1, [1,2]))
# print(numbers.index(3))
# print(numbers.count(3))
#
# numbers = list(numbers)
# print(numbers)
# numbers.clear()
# numbers = tuple(numbers)
# print(numbers)