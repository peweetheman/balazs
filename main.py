
def minimum(list):
    # return the smallest element in the list
    smallest_seen = 1000000000000
    for i in list:
        if i < smallest_seen:
            smallest_seen = i
    return smallest_seen

def sort(list):
    # return a sorted list in increasing order
    sorted_list = []

    while len(list) > 0:
        smallest_element = minimum(list)
        sorted_list.append(smallest_element)
        list.remove(smallest_element)

    return sorted_list

print(sort(list=[5, 2, 4, 3, 7, 9]))  # should return [2,3,4,5,7,9]
print(sort(list=[92340820943, 3249082093480, 324082093482, 29048209, 932482904820, 23490820948, 23490823904]))
