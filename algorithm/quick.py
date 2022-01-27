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
        bar[low].bar_mark()
        bar[high].bar_mark()

        # Move the left index to the right while it is less than pivot
        while arr[i] < pivot:
            bar[i].bar_check()
            drawAll()
            i += 1
            bar[i-1].bar_done()

        # Move the right index to the left while it is less than pivot
        while arr[j] > pivot:
            bar[j].bar_check()
            drawAll()
            j -= 1
            bar[j+1].bar_done()

        # if index crossed return point
        if i >= j:
            bar[low].bar_done()
            bar[high].bar_done()
            drawAll()
            return j

        temp = arr[i]
        setArr(arr, bar, i, arr[j])
        setArr(arr, bar, j, temp)
        bar[i].bar_move()
        bar[j].bar_move()
        drawAll()

        bar[i].bar_done()
        bar[j].bar_done()
        checkInterrupt()

def q_sort(drawAll, bar, arr, low, high):
    if low >= 0 and high >= 0 and low < high:
        point = partition(drawAll, bar, arr, low, high)

        # divides array into partitions
        q_sort(drawAll, bar, arr, low, point)
        q_sort(drawAll, bar, arr, point + 1, high)