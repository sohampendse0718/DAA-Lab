arr = [10, 7, 8, 9, 1, 5]


def partition(low, high):
    pivot = arr[low]

    i = low + 1
    j = high

    while i <= j:

        while i <= high and arr[i] <= pivot:
            i += 1

        while j >= low and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j


def quick_sort(low, high):
    if low < high:
        pi = partition(low, high)

        quick_sort(low, pi - 1)
        quick_sort(pi + 1, high)


quick_sort(0, len(arr) - 1)

print(arr)