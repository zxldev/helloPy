from PIL import Image

im = Image.open('simple.jpg')
print(im.format, im.size, im.mode)

im.thumbnail((900, 600))
im.save('thumbn.jp','PNG')

