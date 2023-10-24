my_list = [1, 2, 5, 4, 6, 4, 3, 3, 2, 6, 9]

for i in range(len(my_list)-1, 0, -1):
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]

        #print(left.right)
        if left > right:
            my_list[j].mylist[j+1]