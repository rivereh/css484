from PIL import Image, ImageTk, ImageColor
import glob, os

images = glob.glob('images/*.jpg')

testImage = Image.open(images[0])
print(ImageColor.getrgb(testImage))

