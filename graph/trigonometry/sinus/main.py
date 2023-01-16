from PIL import Image
import math

pixel = Image.open("pixel_white.png")
image = Image.open("sinus.png")
line = Image.open("line.png")

y=250
f=2
for x in range(360):
    y -= ((math.sin(math.radians(x))*10)/5)*f
    print(y)
    image.paste(pixel,(x,int(y)),pixel)

for x in range(360,720):
    y += ((math.sin(math.radians(x))*10)/5)*f
    image.paste(pixel,(x,int(y)),pixel)

image.paste(line,(0,250),line)
image.save("sinus.png")
