from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpeg')
# print(filter_image.mode)
# print(filter_image.size)
# print(filter_image.format)

# print(dir(img))

# filter_image = img.filter(ImageFilter.BLUR)
# filter_image.save('blur_pikachu.png', 'png')

filter_image = img.convert('L')
filter_image.show()

resized_image = filter_image.resize((300, 300))
resized_image.show()

filter_image.save('gray_pikachu.png', 'png')
resized_image.save('resized_gray_pikachu.png', 'png')

# filter_image.thumbnail((300, 300))