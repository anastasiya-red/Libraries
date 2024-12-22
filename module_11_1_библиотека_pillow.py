from PIL import Image

image = Image.open('name image.jpg')
print(image.format, image.size, image.mode)

r, g, b = image.split()
image = Image.merge("RGB", (b, r, r))

image = image.resize((500, 600)) #изменение размера
image = image.rotate(180)# поворот изображения

image.show()
image.save('new image.png')
