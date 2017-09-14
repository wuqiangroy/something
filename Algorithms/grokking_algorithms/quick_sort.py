

def quick_sort(array):
    if not isinstance(array, list):
        return "Type Error"
    if len(array) < 2:
        return array
    pivot = array[0]
    low = [i for i in array[1:] if i < pivot]
    bigger = [i for i in array[1:] if i >= pivot]
    return quick_sort(low) + [pivot] + quick_sort(bigger)

if __name__ == "__main__":
    array = [2, 3, 0, 1, 3, 6, 4, 1, 7, 8, 3, 2, 1]
    print(quick_sort(array))
