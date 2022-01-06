from visualize.manager import setArr, checkInterrupt

# Shell Sort by Timo Bingmann #https://panthema.net/2013/sound-of-sorting/
# with gaps by Robert Sedgewick from http://www.cs.princeton.edu/~rs/shell/shell.c
def Shell(drawAll, bar, arr):
    size = len(arr)
    incs = [1391376, 463792, 198768, 86961, 33936
            , 13776, 4592, 1968, 861, 336
            , 112, 48, 21, 7, 3, 1 ]
            
    done = False

    while not done:
        for check in range(size - 1):
            if arr[check] > arr[check + 1]:

                # start
                for k in range(len(incs)):
                    if incs[k] < size:
                        gap = incs[k]

                        for i in range(gap, size):
                            temp = arr[i]
                            j = i

                            bar[j].bar_check()
                            drawAll()

                            while j >= gap and arr[j - gap] > temp:
                                bar[j].bar_move()
                                drawAll()

                                setArr(arr, bar, j, arr[j - gap])
                                j -= gap

                            bar[j].bar_move()
                            drawAll()

                            setArr(arr, bar, j, temp)
                            drawAll()

                            checkInterrupt()

            else:
                done = True

# 
            #     gap = size // 2
            #     while gap > 0:
            #         for i in range(gap, size):
            #             temp = arr[i]
            #             j = i

            #             while j >= gap and arr[j - gap] > temp:
            #                 arr[j] = arr[j - gap]
            #                 j -= gap

            #             for event in pygame.event.get():
            #                 if event.type == pygame.QUIT:
            #                     pygame.quit()
            
            #                 arr[j] = temp
            #         gap //= 2

            # else:
            #     done = True
#