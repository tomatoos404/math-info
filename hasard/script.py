# from random import *
# list = []
# for i in range(100):
#     list.append(randint(1, 100))
# print(list)
# print(len(list))

from random import *
result = []
for i in range(3):
    result.append(randint(1, 6))
print(result)
print(sum(result))