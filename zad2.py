def Sort(unsorted):

        return (sorted(unsorted, key=lambda x: (x[1],x[2])))

list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]

print(Sort(list_to_sort))