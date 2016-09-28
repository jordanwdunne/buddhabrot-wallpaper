import math
import sys
import pygame
from pygame import gfxdraw
from pygame import Color
pygame.init()

def getScreen(height, width, iterations, screenName):
    print screenName + " Rendering has started"
    screen = [[0] * height for i in range(width)]
    for x in range(width):
        if x % (width/10) == 0 and x != 0:
            showProgress(x/(width/100))
        for y in range(height):
            c = complex(((x * 3.) / width) - 2, ((y * 2.0) / height) - 1)
            z = c
            complex_sequence = set([])
            for i in range(iterations):
                complex_sequence.add(z)
                z = z ** 2 + c
                if (z.real * z.real + z.imag * z.imag) > 4:
                    complex_sequence.add(z)
                    for term in complex_sequence:
                        pixel_x = math.floor(((term.real + 2) * width) / 3.)
                        pixel_y = math.floor(((term.imag + 1) * height) / 2.)
                        if 0 <= pixel_x < width and 0 <= pixel_y < height:
                            screen[int(pixel_x)][int(pixel_y)] += 1
                    break

    minimum = screen[0][0]
    maximum = screen[0][0]
    for x in range(width):
        for y in range(height):
            if screen[x][y] < minimum:
                minimum = screen[x][y]
            if screen[x][y] > maximum:
                maximum = screen[x][y]

    print screenName + " Rendering has finished" + '\n'
    return (screen, minimum, maximum)

def drawColorMandel(height, width, redIteration, blueIteration, greenIteration):
    redTuple = getScreen(height, width, redIteration, "Red Channel")
    greenTuple = getScreen(height, width, greenIteration, "Green Channel")
    blueTuple = getScreen(height, width, blueIteration, "Blue Channel")

    redScreen = redTuple[0]
    greenScreen = greenTuple[0]
    blueScreen = blueTuple[0]

    redMin = redTuple[1]
    greenMin = greenTuple[1]
    blueMin = blueTuple[1]

    redMax = redTuple[2]
    greenMax = greenTuple[2]
    blueMax = blueTuple[2]


    for x in range(width):
        for y in range(height):
            redChannel = ((redScreen[x][y] - redMin) * 255) / (redMax - redMin)
            greenChannel = ((greenScreen[x][y] - greenMin) * 255) / (greenMax - greenMin)
            blueChannel = ((blueScreen[x][y] - blueMin) * 255) / (blueMax  - blueMin)
            gfxdraw.pixel(window, x, y, Color(redChannel, greenChannel,  blueChannel, 255))

    pygame.display.flip()

def drawSingleMandel(height, width, iteration, screenName):
    screenTuple = getScreen(height, width, iteration, screenName)
    screen = screenTuple[0]
    screenMin = screenTuple[1]
    screenMax = screenTuple[2]

    for x in range(width):
        if x % (width/10) == 0 and x != 0:
            showProgress(x/(width/100))
        for y in range(height):
            color = ((redScreen[x][y] - redMin) * 255) / (redMax - redMin)
            gfxdraw.pixel(window, x, y, Color(color, color,  color, 255))

    pygame.display.flip()

def showProgress(percentProgress):
    progress = int(percentProgress)/10
    print "[" + (progress - 1)*"=" + ">" + (10-progress)*"."+"] " + str(progress * 10) + "%"

if __name__ == '__main__':
    width = 4500
    height = 3000
    redIteration = 10
    greenIteration = 40
    blueIteration = 100

    window = pygame.display.set_mode((width, height))

    drawColorMandel(height, width, redIteration, blueIteration, greenIteration)
    pygame.image.save(window, "wallpaper.png")
    pygame.display.quit()
