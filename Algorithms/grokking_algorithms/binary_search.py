from math import ceil


def search(sort_list, num):
    """
    receive a sorted list and a number
    return the index of number in list
    using binary search
    """

    low = 0
    high = len(sort_list) - 1
    while low <= high:
        index = ceil((low+high)/2)
        if sort_list[index] == num:
            return index
        elif sort_list[index] > num:
            high = index
        else:
            low = index


if __name__ == "__main__":
    print(search([1, 4, 7, 21, 33, 55, 100, 122, 134, 156], 134))
