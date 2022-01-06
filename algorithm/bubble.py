from visualize.manager import setArr, checkInterrupt

def Bubble(drawAll, bar, arr):
    size = len(arr)
    done = False

    while not done:
        for check in range(size - 1):
            if arr[check] > arr[check + 1]:

                # start
                for i in range(size - 1):
                    for j in range(0, size - i - 1):
                        bar[j].bar_check()
                        drawAll()

                        if arr[j] > arr[j + 1]:
                            bar[j].bar_move() 
                            drawAll()

                            temp = arr[j]
                            setArr(arr, bar, j, arr[j + 1])
                            setArr(arr, bar, j + 1, temp)

                        bar[j].bar_done()
                        drawAll()

                        checkInterrupt()

            else:
                done = True   
                