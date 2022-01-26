import pygame
import sys
from visualize import *
from algorithm import Bubble, Shell, Merge, Insertion, Quick

pygame.init()
clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm")

ResetButton = Button(5, 10, 60, 30, [B_COLOR, B_HOVER], "RESET", 15)

AlgDrop = Dropdown(75, 10, 120, 30, [DROP_COLOR, DROP_HOVER], [B_COLOR, B_HOVER],
                "Algorithm", ["Bubble Sort", "Insertion Sort", "Shell Sort", "Merge Sort", "Quick Sort"], 15)

StartButton = Button(205, 10, 60, 30, [B_COLOR, B_HOVER], "START", 15)

ArraySlider = Slider(275, 10, 300, 30, 85, SLI_BOX, SLI_BUTTON, MIN_VAL, MAX_VAL, START_VAL, 
                    "Array Size", 11, 16)

def drawAll(SCREEN, bar, pos):
    SCREEN.fill(BLACK)

    # draw Array
    for arr in bar:
        arr.draw(SCREEN)

    # draw Button
    ResetButton.draw(SCREEN, pos)
    AlgDrop.draw(SCREEN, pos)
    StartButton.draw(SCREEN, pos)
    ArraySlider.draw(SCREEN, pos)

    pygame.display.update()


def main():
    size = ArraySlider.get_val()
    arr = makeArr(size)
    bar = toBar(arr, size)

    Algorithm = -1

    run = True

    while run:
        clock.tick(60)
        mouse = pygame.mouse.get_pos()
        event_list = pygame.event.get()
        drawAll(SCREEN, bar, mouse)

        size = ArraySlider.get_val()

        for event in event_list:
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pass
                # g = findBar(bar, 4)
                # setBar(arr, bar, g, arr[g+1])

            if pygame.mouse.get_pressed()[2]:
                print(arr)
                print(bar)
                temp = arr[0]
                setArr(arr, bar, 0, arr[1])
                setArr(arr, bar, 1, temp)
                print(arr)
                print(bar)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Bubble(lambda: drawAll(SCREEN, bar, mouse), bar, arr)
                if event.key == pygame.K_2:
                    Insertion(lambda: drawAll(SCREEN, bar, mouse), bar, arr)
                if event.key == pygame.K_3:
                    Shell(lambda: drawAll(SCREEN, bar, mouse), bar, arr)
                if event.key == pygame.K_4:
                    Merge(lambda: drawAll(SCREEN, bar, mouse), bar, arr)
                
                if event.key == pygame.K_c:
                    arr = makeArr(size)
                    bar = toBar(arr, size)

                if event.key == pygame.K_ESCAPE:
                    run = False
        
        reset_click = ResetButton.is_click(mouse, event_list)
        start_click = StartButton.is_click(mouse, event_list)

        alg_choose = AlgDrop.is_choose(mouse, event_list)

        ArraySlider.is_hold(mouse, event_list)

        if reset_click:
            arr = makeArr(size)
            bar = toBar(arr, size)

        if alg_choose != -1:
            AlgDrop.main = AlgDrop.options[alg_choose]
            Algorithm = alg_choose

        if start_click:
            if Algorithm == 0:
                Bubble(lambda: drawAll(SCREEN, bar, mouse), bar, arr)
            if Algorithm == 1:
                Insertion(lambda: drawAll(SCREEN, bar, mouse), bar, arr)
            if Algorithm == 2:
                Shell(lambda: drawAll(SCREEN, bar, mouse), bar, arr)
            if Algorithm == 3:
                Merge(lambda: drawAll(SCREEN, bar, mouse), bar, arr)
            if Algorithm == 4:
                Quick(lambda: drawAll(SCREEN, bar, mouse), bar, arr)

    pygame.quit()
    sys.exit()

main()