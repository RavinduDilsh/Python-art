
from PIL import Image
import sys

path=sys.argv[0]
img=Image.open('nipun.png')

width,height=img.size
aspect_ratio=height/width
new_weidth=100
new_height=aspect_ratio*new_weidth
img=img.resize((new_weidth,int(new_height)))

img=img.convert('L')
pixels=img.getdata()

charactor=["B","#","S","@","$","*","+","!",":",",","."]

new_pixels=[charactor[pixels//25] for pixels in pixels]
new_pixels=''.join(new_pixels)

new_pixel_count=len(new_pixels)
final_image=[new_pixels[index:index+new_weidth] for index in range(0,new_pixel_count,new_weidth)]
final_image='\n'.join(final_image)

with open("3.text","w") as f:
    f.write(final_image)
