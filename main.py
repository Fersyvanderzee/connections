from figures import *
from PIL import Image

img_width, img_height = 1000, 1000

image = Image.new('RGB', (img_width, img_height))


fig = Figures(line_w_big=5, line_w_small=2, image=image)


fig.draw_diamond(center_xy=(img_width/2, img_height/2), size=100)
fig.draw_rectangle(filled=True, start_xy=(200, 200), size=(100, 200))
fig.draw_circle(filled=False, center_xy=(700, 700), size=100)

image.show()

