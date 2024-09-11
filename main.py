# By David Krljanovic
# 2022 - 07 - 23
# the main that calls image processing functions.

import myImageManip
import cmpt120image

print("Welcome to Image Processor!\n")

print("Here are your options")
print("0: Quit")
print("1: Interlace with black lines")
print("2: Invert the colour of the image")
print("3: Convert the colour of the image into grayscale")
print("4: Adjust the saturation")

check = True

while True:
    img = cmpt120image.getImage("ngc3132.jpg")

    choice = input("Enter your choice (0/1/2/3/4):\n")
    choice = int(choice)

    # Validate input
    if choice < 0 or choice > 4:
        print("Sorry, I don’t understand " + str(choice) + ", please try again")

    # option 0: quit program
    elif choice == 0:
        print("Goodbye.")
        break

    elif choice == 1:
        myImageManip.interlace()

    elif choice == 2:
        myImageManip.invert()

    elif choice == 3:
        myImageManip.greyscale()

    elif choice == 4:
        myImageManip.saturation()
