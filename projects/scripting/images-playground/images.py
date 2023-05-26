from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpeg')
filter_image = img.filter(ImageFilter.BLUR)

# print(dir(img))
filter_image.save('blur_pikachu.png', 'png')