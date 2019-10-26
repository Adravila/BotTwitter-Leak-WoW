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

    text_ = "» Who will be the villain of this expansion?? "+str(array[i])
    draw.text((30, y+240), text_, font=font_, fill="white",align="center")

    image.save("foto.png")

# Parte del Bot - WoW Leaks generator #

print('Iniciando Bot de @BotLeaksGen')

CONSUMER_KEY = '0Tg5rkZu2fwkCa7sLw4eoYWww'
CONSUMER_SECRET = 'XteqYferF3kKeQpuv44r7K3TwP5RxlJtrlptGzc4SfBt9jIOQS'
ACCESS_KEY = '1187846994171256832-YiVthHx3FUCACyLcfObSSGTWre1x4O'
ACCESS_SECRECT = 'rVNCrFxeBaGyyKrkbVtMtdnMiac6hViQUsU7kcPfGDQ0b'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRECT)

api = tweepy.API(auth)
api.sleep_on_rate_limit = True

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                            last_seen_id,
                            tweet_mode='extended')

    for mention in mentions:
        print((str(mention.id) +" - "+ mention.full_text).encode('utf-8').strip())
        generateImage()
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        api.update_with_media(  filename="foto.png",
                                status='@' + mention.user.screen_name +" How could the next expansion of World of Warcraft be?",
                                in_reply_to_status_id=last_seen_id)
while True:
    reply_to_tweets()
    time.sleep(15)

