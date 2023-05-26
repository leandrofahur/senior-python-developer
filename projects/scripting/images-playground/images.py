from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpeg')
# print(dir(img))

# filter_image = img.filter(ImageFilter.BLUR)
# filter_image.save('blur_pikachu.png', 'png')

filter_image = img.convert('L')
filter_image.save('gray_pikachu.png', 'png')