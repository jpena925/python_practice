import sys
import os
from PIL import Image

#grab first and second argument with sys
jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

#check if second argument exists and if not, create it for the new pngs
if not os.path.exists(png_folder):
    os.makedirs(png_folder)

#loop through pokedex
for filename in os.listdir(jpg_folder):
    img = Image.open(f'{jpg_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{png_folder}{clean_name}.png', 'png')
    print('done!')

#convert to PNG
#save to the new folder

