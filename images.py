from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

#saves a new file as blurred
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")