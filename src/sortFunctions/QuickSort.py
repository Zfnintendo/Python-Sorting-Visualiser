def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high):

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] < pivot:

            i += 1

            swap(arr, i, j)

            yield arr

    swap(arr, i + 1, high)

    yield arr

    return i + 1


def quickSort(arr, low, high):

    if low < high:

        # Get all the states from partition()
        partition_steps = partition(arr, low, high)

        try:
            while True:
                yield next(partition_steps)

        except StopIteration as e:
            pi = e.value

        # Sort left side
        yield from quickSort(arr, low, pi - 1)

        # Sort right side
        yield from quickSort(arr, pi + 1, high)


class QuickSort:

    def Sort(self, arr):

        yield from quickSort(arr, 0, len(arr) - 1)