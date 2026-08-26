# To heapify a subtree rooted with node i
def heapify(arr, n, i):

    # Initialize largest as root
    largest = i

    # Left index = 2*i + 1
    l = 2 * i + 1

    # Right index = 2*i + 2
    r = 2 * i + 2

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:

        arr[i], arr[largest] = arr[largest], arr[i]

        yield arr

        yield from heapify(arr, n, largest)


class HeapSort:

    def Sort(self, arr):

        n = len(arr)

        # Build heap
        for i in range(n // 2 - 1, -1, -1):
            yield from heapify(arr, n, i)

        # One by one extract an element from heap
        for i in range(n - 1, 0, -1):

            # Move current root to end
            arr[0], arr[i] = arr[i], arr[0]

            yield arr

            # Heapify the reduced heap
            yield from heapify(arr, i, 0)