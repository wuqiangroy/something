

def find_smallest(arr):
    """to find the smallest number in lis"""

    index = 0
    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index


def select_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))

    return sorted_arr

if __name__ == "__main__":
    print(select_sort([1, 5, 2, 0, 11, 3, 555, 18, 12, 43]))
