from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')

#saves a new file as blurred
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

#rotate
filtered_img.rotate(90)

#resize
filtered_img.resize((300,300))

#resize to thumbnail keeping aspect ratio
filtered_img.thumbnail((400,200)) #will try to match the given size to its best guess
filtered_img.save('thumbnail.jpg')

#cropping
box = (100,100,400,400)
region = filtered_img.crop(box)


filtered_img.show()
