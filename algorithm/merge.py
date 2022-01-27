from visualize.manager import setArr, checkInterrupt

def Merge(drawAll, bar, arr):
    size = len(arr)
    done = False

    while not done:
        for check in range(size - 1):
            if arr[check] > arr[check + 1]:

                # start
                m_sort(drawAll, bar, arr, 0, len(arr))

            else:
                done = True


def sort(drawAll, bar, arr, start, mid, end):
    bar[start].bar_check()
    bar[end - 1].bar_mark()
    drawAll()

    temp = [None] * (end - start)
    i = start
    j = mid
    k = 0

    # Keep merged and sorted array to temp[]
    while i < mid and j < end:
        if arr[i] > arr[j]:
            bar[j].bar_mark()
            temp[k] = arr[j]
            j += 1

        else:
            bar[i].bar_mark()
            temp[k] = arr[i]
            i += 1

        k += 1
        drawAll()

    # Copy any elements left 
    while i < mid:
        bar[i].bar_mark()
        temp[k] = arr[i]
        i += 1
        k += 1
        drawAll()

    while j < end:
        bar[j].bar_mark()
        temp[k] = arr[j]
        j += 1
        k += 1
        drawAll()

    # Output sorted array
    for i in range(end - start):
        bar[start + i].bar_move()
        drawAll()

        setArr(arr, bar, start + i, temp[i])

        checkInterrupt()

    drawAll()


def m_sort(drawAll, bar, arr, start, end):
    if start + 1 < end:
        mid = (start + end) // 2
        
        # Calling the first half of array
        m_sort(drawAll, bar, arr, start, mid)

        # Calling the second half of array
        m_sort(drawAll, bar, arr, mid, end)

        # Sorting and merging the halves sorted array
        sort(drawAll, bar, arr, start, mid, end)
