from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import os
from PIL import Image, ImageFont, ImageDraw
from instabot import Bot

import random

user_name = 'xxxx'
password = 'xxxx'
IMAGE_WIDTH = 1080
IMAGE_HEIGHT = 1080
POS_X = 220
POS_Y = 150
MARGIN_RIGHT = 220
MARGIN_BOTTOM = 150
HOMEURLBASE = 'https://www.brainyquote.com/topics/life-quotes_'
OUTPUT_FILENAME = 'immagine.jpg'
FONT = 'GloriaHallelujah-Regular'
FONT_SIZE = 64

def get_quote():
    """Return the tuple (quote, author)
    Quote and author are scraped from the HOMEURLBASE site
    """

    # Choose a random page of the site
    pagenumber = random.randint(1, 22)
    homeurl = HOMEURLBASE + str(pagenumber)
    p = os.path.abspath('chromedriver')
    if not os.path.exists(p):
        raise("It is not possible to find the chromedrive")
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        browser = webdriver.Chrome(executable_path=p, options=options)
        browser.get(homeurl)
    except (WebDriverException) as err:
        print("Something go wrong, please make sure to have the correct chromedriver")
        raise

    soup = BeautifulSoup(browser.page_source, "html.parser")
    title = soup.find_all("a", class_="b-qt")
    authors = soup.find_all("a", class_="bq-aut")
    # Check if scraping works
    if len(title) == 0 or len(authors) == 0:
        print("Parsing error")
        raise ValueError
    index = random.randint(0, len(title)-1)
    # Choose a random quote from the list
    quote = title[index].get_text()
    author = authors[index].get_text()
    return (quote,author)

def choose_quote(img, font):
    """Return the quote that fit the image with the given parameters of margin"""
    quote = ''
    imgdraw = ImageDraw.Draw(img)
    while 1:
        quotestring = ''
        quote, author = get_quote()
        for word in quote.split():
            # Add a word at the time and check if text exceeds the right margin,
            # if it does, go the new line
            margin = imgdraw.multiline_textsize((quotestring + word), font=font)
            if (img.width - POS_X - margin[0] < MARGIN_RIGHT):
                quotestring = quotestring + '\n' + word + ' '
            else:
                quotestring += word + ' '
        # Check if text exceeds the bottom margin
        margin = imgdraw.multiline_textsize((quotestring + '\n\n' + author), font=font)
        if (img.height - POS_Y - margin[1] > MARGIN_BOTTOM):
            quote = quotestring + '\n\n' + author
            break

    return (quote)

def get_quoted_image():
    """Create the image with a quote on it and save it"""
    img = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, FONT_SIZE)
    quote = choose_quote(img, font)
    draw.multiline_text((POS_X, POS_Y), quote, fill=(64, 64, 64), font=font)
    img.show()
    try:
        img.save(OUTPUT_FILENAME)
    except (ValueError, OSError) as err:
        print("Impossible to save the image")
        raise


def create_tags_list(quote=None):
    """Return the caption string for description made by tags"""
    tags = ['quotes']
    captionstring = quote + ' ' if quote else ''
    for word in tags:
        captionstring += '#' + word + ' '

    return(captionstring)

def upload_image(captionstring=None):
    """Upload the created image to the Instagram account"""
    prompt = input("Do you want upload?")
    if int(prompt) == 1:
        # Check if the image generated exists
        if not os.path.exists(OUTPUT_FILENAME):
            print("Image deleted")
            raise ValueError
        try:
            bot = Bot()
            bot.login(username=user_name, password=password)
            bot.upload_photo(OUTPUT_FILENAME, caption=captionstring)
        except:
            print("Instagram login/uploading error")
            raise ValueError


def main():
    try:
        get_quoted_image()
        upload_image(create_tags_list())
    except Exception as err:
        print("An error occurs. Quitting...")
        print(err)

if __name__ == "__main__":
    main()

