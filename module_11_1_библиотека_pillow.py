from PIL import Image

image = Image.open('name image.jpg')
print(image.format, image.size, image.mode)

r, g, b = image.split()
image = Image.merge("RGB", (g, r, b))

image = image.resize((500, 700)) #изменение размера
image = image.rotate(45)# поворот изображения

image.show()
image.save('new image.png')
