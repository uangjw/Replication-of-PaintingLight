import cv2
import sys
from myProj import run

image = cv2.imread(sys.argv[1])
mask = None

ambient_intensity = 0.45
light_intensity = 0.95
light_source_height = 1.0
stroke_density_clipping = 1.2

light_color_red = 1.0
light_color_green = 1.0
light_color_blue = 1.0

run(image, mask, ambient_intensity, light_intensity, light_source_height,
    stroke_density_clipping, light_color_red,
    light_color_green, light_color_blue)
