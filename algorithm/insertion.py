from visualize.manager import setArr, checkInterrupt

def Insertion(drawAll, bar, arr):
    size = len(arr)
    done = False

    while not done:
        for check in range(size - 1):
            if arr[check] > arr[check + 1]:

                # start
                for i in range(1, size):
                    temp = arr[i]
                    j = i - 1

                    while j >= 0 and arr[j] > temp:
                        bar[j].bar_check()
                        bar[j + 1].bar_move()
                        drawAll()

                        setArr(arr, bar, j + 1, arr[j])
                        
                        if j + 1 == i:
                            bar[j + 1].bar_mark()

                        bar[j].bar_done()
                        drawAll()

                        j -= 1
                   
                    bar[j + 1].bar_move()
                    drawAll()

                    setArr(arr, bar, j + 1, temp)

                    checkInterrupt()

            else:
                done = True