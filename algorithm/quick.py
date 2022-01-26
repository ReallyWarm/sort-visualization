from visualize.manager import setArr, checkInterrupt
import math

def Quick(drawAll, bar, arr):
    size = len(arr)
    done = False

    while not done:
        for check in range(size - 1):
            if arr[check] > arr[check + 1]:

                # start
                q_sort(drawAll, bar, arr, 0, size - 1)

            else:
                done = True

def partition(drawAll, bar, arr, low, high):
    # Value in the middle of the array
    pivot = arr[math.floor((low + high) / 2)]
    # Left most index
    i = low
    # Right most index
    j = high

    while 1:
        # Move the left index to the right while it is less than pivot
        while arr[i] < pivot:
            i += 1
        # Move the right index to the left while it is less than pivot
        while arr[j] > pivot:
            j -= 1

        # if index crossed return point
        if i >= j:
            return j

        temp = arr[i]
        setArr(arr, bar, i, arr[j])
        setArr(arr, bar, j, temp)
        drawAll()

        checkInterrupt()

def q_sort(drawAll, bar, arr, low, high):
    if low >= 0 and high >= 0 and low < high:
        point = partition(drawAll, bar, arr, low, high)

        # divides array into partitions
        q_sort(drawAll, bar, arr, low, point)
        q_sort(drawAll, bar, arr, point + 1, high)