# for item in range(10):
#     print(item)

# total = 0
# prices = [10, 20, 30]
# for item in prices:
#     total += item
# print(f"total = {total}")    

# nested loops
# for x in range(3):
#     for y in range(2):
#         print(f'({x},{y})')

numbers = [2, 2, 2, 2, 7]
for item in numbers:
    output = ''
    for x in range(item):
        output += 'x'
    print(output)    
