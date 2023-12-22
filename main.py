from shape import *
from PIL import Image
import random

"""

PURELY FOR TESTING PURPOSES.

"""

img_width, img_height = 3000, 3000
margin = 100

bg_color = (185, 32, 39)

image = Image.new(mode='RGB', size=(img_width, img_height), color=bg_color)

for j in range(5):
    for i in range(1000):
        filled = random.choice([True, False])
        center_xy = (
            random.randint(margin, img_height - margin),
            random.randint(margin, img_height - margin)
        )

        size = random.randint(15, 60)

        Diamond(image=image, filled=filled, center_xy=center_xy, size=size)


    image.show()
