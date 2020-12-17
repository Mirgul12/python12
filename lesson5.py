from datetime import datetime
#
# start = datetime.now()
#
# nums = [num for num in range(200000)]
# # print(nums)
# finish = datetime.now()
# start2 = datetime.now()
# nums2 = []
# for i in range(20):
#     nums2.append(i)
# # print(nums2)
# finish2 = datetime.now()

#
# even = [num for num in range(50) if num % 2 == 1 and num % 10 ==0]
# print(even)

# my_func = lambda x, y: x+y
# my_func()
#
# def add(x,y):
#     return x+y
# print(add(10,10))

# list_= [1,2,3,4,5,6,7,8,9]
# def my_func(x):
#     return x ** x
#
# new_list = list(map(my_func,list_))
# print(new_list )
#
# nums = [1,2,3,4,5]
# def my_func(x):
#     x += 10
#     return x
# nums2 = list(map(my_func, nums ))
# print(nums2)

# text = 'i love python'
#
# def my_func(x):
#     return x.upper()
#
# text2 = list(map(my_func,text))
# print(text2)
# text3 = ''.join(text2)
# print(text3)
#
# mixed = ['мак','просо','мак','просо','мак','мак',]
# my_filter = lambda x:x == 'мак'
# zolushka = list(filter(my_filter,mixed))
# print(zolushka)

from functools import reduce
# nums = [x for x in range (50)]
# lambda_func = lambda x,y:x+y
# sum_all = reduce(lambda_func,nums)
# print(sum_all )

# text = 'hello world'
# nums = [x for x in range(20)]
# tuple_ = ('a', 'b',' c',' d' ,'e')
#
# zip_func = list(zip(text,nums,tuple_))
# print(zip_func)
# tuple_ = tuple(zip(text,nums))
# print(tuple_)

