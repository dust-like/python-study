import shutil
import sys 
from PIL import Image

sys.setrecursionlimit(1000000)

img_filename = 'img/图片.png'
img_ed_filename = 'img_ed/图片_ed.png'
new_color = (255,0,0,255)
old_color = (255,255,255,255)

shutil.copyfile(img_filename,img_ed_filename)
im = Image.open(img_ed_filename)

ipt = input('请输入起始坐标，以半角逗号隔开：')
coordinate = ipt.split(',')
coordinate[0] = int(coordinate[0])
coordinate[1] = int(coordinate[1])
def Color_Fill(x,y,o_c,n_c):
	if(im.getpixel((x,y)) == o_c):
		im.putpixel((x,y),n_c)
		Color_Fill(x,y+1,o_c,n_c)
		Color_Fill(x,y-1,o_c,n_c)
		Color_Fill(x-1,y,o_c,n_c)
		Color_Fill(x+1,y,o_c,n_c)
Color_Fill(coordinate[0],coordinate[1],old_color,new_color)
im.save(img_ed_filename)
