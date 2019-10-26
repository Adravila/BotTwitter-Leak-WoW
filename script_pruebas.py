from PIL import Image, ImageDraw, ImageFont
import random
import tweepy
import time

def generateImage():
    image = Image.open("background.png")
    draw = ImageDraw.Draw(image)

    #!- title -!#
    with open('name_expansions.txt') as f:
        array = f.readlines()
    i = random.randint(0, array.__len__()-1)

    text = str(array[i])
    lines = text.splitlines()
    font = ImageFont.truetype("WoW-SlF-Bold.ttf", 20)
    h = font.getsize(text)[1] * len(lines)
    w = font.getsize(max(lines, key=lambda s: len(s)))[0]
    x, y = image.size
    x /= 2
    x -= w / 2
    y /= 6
    draw.text((x, y), text, font=font, fill="white",align="center")

    font_ = ImageFont.truetype("calibri.ttf", 22)
    y = 120

    #!- description 1 -!#
    with open('class.txt') as f:
        array = f.readlines()
    i = random.randint(0, array.__len__() - 1)

    text_ = "» New class available: "+str(array[i])
    draw.text((30, y), text_, font=font_, fill="white",align="center")

    #!- description 2 -!#
    with open('races.txt') as f:
        array = f.readlines()
    i = random.randint(0, array.__len__() - 1)

    text_ = "» New allied race (neutral): "+str(array[i])
    draw.text((30, y+30), text_, font=font_, fill="white",align="center")


    #!- description 3 -!#
    with open('new_world.txt') as f:
        array = f.readlines()
    i = random.randint(0, array.__len__() - 1)

    text_ = "» New world to explore: "+str(array[i])
    draw.text((30, y+60), text_, font=font_, fill="white",align="center")

    #!- description 4 -!#
    with open('theme.txt') as f:
        array = f.readlines()
    i = random.randint(0, array.__len__() - 1)

    text_ = "» Core theme: "+str(array[i])
    draw.text((30, y+90), text_, font=font_, fill="white",align="center")

    #!- description 5 -!#

    op = "No"
    i = random.randint(0, 1)
    if i == 1:
        op = "Yes"
    else:
        op = "No"

    text_ = "» Will there be Level Squish? "+op
    draw.text((30, y+120), text_, font=font_, fill="white",align="center")

    #!- description 6 -!#
    i = random.randint(0, 1)
    if i == 1:
        op = "Yes"
    else:
        op = "No"

    text_ = "» Will there be World Revamp? "+op
    draw.text((30, y+150), text_, font=font_, fill="white",align="center")

    #!- description 7 -!#
    i = random.randint(0, 1)
    if i == 1:
        op = "Yes"
    else:
        op = "No"

    text_ = "» Will there be Player Housing? "+op
    draw.text((30, y+180), text_, font=font_, fill="white",align="center")

    #!- description 8 -!#
    i = random.randint(0, 1)
    if i == 1:
        op = "Yes"
    else:
        op = "No"

    text_ = "» Will there be Guild Halls? "+op
    draw.text((30, y+210), text_, font=font_, fill="white",align="center")
    
    #!- description 9 -!#
    with open('villain.txt') as f:
        array = f.readlines()
    i = random.randint(0, array.__len__() - 1)

    text_ = "» Who will be the villain of this expansion? "+str(array[i])
    draw.text((30, y+240), text_, font=font_, fill="white",align="center")

    image.save("foto.png")

generateImage()