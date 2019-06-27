from PIL import Image

img = Image.open("obamaimage.jpg")
img.show()
print(img.size)