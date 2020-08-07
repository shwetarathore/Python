# matrix = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)

# # list methods/functions
# append, insert, remove, clear, pop, index, count, sort, reverse, copy
# task - removw duplicate nos. from list

list = [1, 2, 2, 3, 4, 6, 5, 5]
uniq = []
# list.sort()
print(list)
for n in list:
    if n not in uniq:
        uniq.append(n)
print(uniq)    
