# a: int = 5
#
#
# def soup(x: int) -> list[int]:
#     '''list range x+1
#
#     :param x: any int
#     :return: list
#     '''
#     return list(i for i in range(x+1))
#
#
# print(soup(a))

import os, fnmatch
listOfFiles = os.listdir('D:\DMS a.v.0.1\images')
pattern = "*.png"
list = []
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            list.append(entry)

print(list)

list[0] = '10 room.png'
list[1] = '11 room.png'
list.sort()

print(list)
