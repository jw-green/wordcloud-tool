from scipy.misc import imread

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def openFile(filename):
    text = open(filename, encoding='utf-8').read()
    return text


def openImage(image_filename):
    image = imread(image_filename)
    return image


def setImageColour(image_handle):
    image_colours = ImageColorGenerator(bg_image)
    return image_colours


def createWordCloud(font_path, image, stopwords, text):
    wordCloud = WordCloud(font_path=font_path, background_color="white",
                          max_words=2000, mask=image, stopwords=stopwords)

    wordCloud.generate(text)

    wordCloud.recolor(color_func=setImageColour(bg_image))

    return wordCloud


def saveWordCloud(wordCloud, filename):
    wordCloud.to_file("output_images/" + filename)


def getValidInput( input_string ):

    user_input = input( input_string )

    if "." not in user_input:
        print("[ERROR] Please enter a valid filename and extension.")
        getValidInput( input_string )
    else:
        return user_input

stopwords = set(STOPWORDS)

filename = getValidInput("Text File Name: ")
text = openFile("ref/srcTxt/" + filename)

image_filename = getValidInput("Image File Name: ")
bg_image = openImage("ref/input_images/" + image_filename)

image_colours = setImageColour(bg_image)

wordCloud = createWordCloud(
    "ref/typefaces/Raleway-Light.ttf", bg_image, stopwords, text)

output_filename = getValidInput("Output File Name: ")
saveWordCloud(wordCloud, output_filename)
