

def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return  array


def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    lower = [i for i in array[1:] if i <= pivot]
    biger = [i for i in array[1:] if i > pivot]
    return quick_sort(lower) + [pivot] + quick_sort(biger)

if __name__ == "__main__":
    array = [1, 2, 6, 5, 7, 3, 0, 1]
    # print(insert_sort(array))
    print(quick_sort(array))
