import pygame
import sys
from numpy.random import shuffle
from .Bar import ArrayBar

def checkInterrupt():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

def makeArr(size):
    arr = [i for i in range(1, size + 1)]
    shuffle(arr)

    return arr

def toBar(arr, size):
    bar = []
    for i, v in enumerate(arr):
        this_arr = ArrayBar(i, v, size)
        bar.append(this_arr)

    return bar

def setArr(arr, bar, index, val):
    arr[index] = val

    bar[index] = ArrayBar(index, val, len(bar))

# def findIndex(arr, val):
#     for i, v in enumerate(arr):
#         if v == val:
#             return i
#     # i = arr.index(val)
#     return i

# def findBar(bar, val):
#     for i, v in enumerate(bar):
#         if v.get_val() == val:
#             return i
#     # i = arr.index(val)
#     return i

# def setBar(arr, bar, index1, val):
#     bar[index1] = ArrayBar(index1, val, len(bar))
#     # bar[index1].bar_check()