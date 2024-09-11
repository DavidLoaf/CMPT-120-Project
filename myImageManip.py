# By David Krljanovic
# 2022 - 07 - 23
# A module that has some simple image processing functions

import cmpt120image


# option 1: interlace (DONE)
def interlace():
    img = cmpt120image.getImage("ngc3132.jpg")
    for row in range(0, 555, 2):
        for col in range(600):
            pixel = img[row][col]
            pixel[0] = 0
            pixel[1] = 0
            pixel[2] = 0
    cmpt120image.saveImage(img, "result-option1.jpg")
    cmpt120image.showImage(img)

# option 2: invert (DONE)
def invert():
    img = cmpt120image.getImage("ngc3132.jpg")
    for row in range(555):
        for col in range(600):
            pixel = img[row][col]
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    cmpt120image.saveImage(img, "result-option2.jpg")
    cmpt120image.showImage(img)

    # option 3: greyscale (DONE)
def greyscale():
    img = cmpt120image.getImage("ngc3132.jpg")
    for row in range(555):
        for col in range(600):
            pixel = img[row][col]
            pixelAvg = (pixel[0] + pixel[1] + pixel[2]) / 3
            pixel[0] = pixelAvg
            pixel[1] = pixelAvg
            pixel[2] = pixelAvg
    cmpt120image.saveImage(img, "result-option3.jpg")
    cmpt120image.showImage(img)

    # option 4: saturation
def saturation():
    img = cmpt120image.getImage("ngc3132.jpg")
    factor = input("by what factor would you like to scale the saturation?")
    factor = float(factor)
    for row in range(555):
        for col in range(500):
            pixel = img[row][col]
            pixelAvg = (pixel[0] + pixel[1] + pixel[2]) / 3
            pixel[0] = pixelAvg + factor*(pixel[0] - pixelAvg)
            pixel[1] = pixelAvg + factor*(pixel[1] - pixelAvg)
            pixel[2] = pixelAvg + factor*(pixel[2] - pixelAvg)
            for i in range(3):
                if pixel[i] > 255:
                    pixel[i] = 255
                elif pixel[i] < 0:
                    pixel[i] = 0

    cmpt120image.saveImage(img, "result-option4.jpg")
    cmpt120image.showImage(img)





