from PIL import Image,ImageFilter
img=Image.open('./pokedex/pikachu.jpg')
filtered_img=img.convert('L')# to convert to grey scale
rotated=filtered_img.rotate(90)
resize=filtered_img.resize((300,300))
box=(100,100,400,400)
region=img.crop(box)
region.save('blur.png','png')



