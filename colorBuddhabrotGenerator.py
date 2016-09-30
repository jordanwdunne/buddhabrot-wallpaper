import math
import sys
import pygame
from pygame import gfxdraw
from pygame import Color
pygame.init()

def getScreen(height, width, iterations, screenName):
    print '\n' + screenName + " Rendering has started"
    screen = [[0] * height for i in range(width)]
    for x in range(width):
        if x % (width/10) == 0:
            showProgress(int((x/(width/100))))
        for y in range(height):
            c = complex(((x * 3.) / width) - 2, ((y * 2.0) / height) - 1)
            z = c
            complexGroup = set([])
            for i in range(iterations):
                complexGroup.add(z)
                z = z ** 2 + c
                if (z.real * z.real + z.imag * z.imag) > 4:
                    complexGroup.add(z)
                    for term in complexGroup:
                        pixelX = math.floor(((term.real + 2) * width) / 3.)
                        pixelY = math.floor(((term.imag + 1) * height) / 2.)
                        if 0 <= pixelX < width and 0 <= pixelY < height:
                            screen[int(pixelX)][int(pixelY)] += 1
                    break

    minimum = screen[0][0]
    maximum = screen[0][0]
    for x in range(width):
        for y in range(height):
            if screen[x][y] < minimum:
                minimum = screen[x][y]
            if screen[x][y] > maximum:
                maximum = screen[x][y]

    print '\n' + screenName + " Rendering has finished" + '\n'
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
            showProgress(int((x/(width/100))))
        for y in range(height):
            color = ((redScreen[x][y] - redMin) * 255) / (redMax - redMin)
            gfxdraw.pixel(window, x, y, Color(color, color,  color, 255))

    pygame.display.flip()

def showProgress(percentProgress):
    tenths = int(percentProgress)/10
    print "[" + (tenths) * ">" + (10 - tenths)*"."+"] " + str(tenths * 10) + "%"

if __name__ == '__main__':
    width = 4500
    height = 3000
    redIteration = 80
    greenIteration = 600
    blueIteration = 4000

    window = pygame.display.set_mode((width, height))
    drawColorMandel(height, width, redIteration, blueIteration, greenIteration)

    savedFilename = str(width) + "x" + str(height) + "_" + str(redIteration) + "_" + str(greenIteration) + "_" + str(blueIteration) + "_" + "wallpaper.png"
    print "Saving final image " + savedFilename

    pygame.image.save(window, savedFilename)
    pygame.display.quit()
