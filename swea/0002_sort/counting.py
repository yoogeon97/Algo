my_list = [1, 2, 5, 4, 6, 4, 3, 3, 2, 6, 9]

counter = [for i in range(10)]

for num i in my_list:
    counter[num] += 1

result = []

for value, count in enumerate(counter):
    for i in range(count):
        result.append(value)

print(result)