import sys
import os
from PIL import Image

# grap first and second arguement
image_folder =sys.argv[1]
output_folder=sys.argv[2]

# check if new/ exist if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through pokedex,
for filename in os.listdir(image_folder):
    img=Image.open(f'{image_folder}{filename}')
    clean_name=os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clean_name}.png",'png')
    print('all done')

# convert image to png

# save to new folder