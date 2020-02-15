from PIL import Image
import tesserocr
 
imag = Image.open('test.jpg')
#imag.show()

imag_gray = imag.convert('L')
#imag_gray.show()
imag_gray.save('gray.jpg')

imag_two = imag_gray.point(lambda x:255 if x>129 else 0)
#imag_two.show()
imag_two.save('two.jpg')

def depoint(imag):
 """传入二值化后的图片进行降噪"""
 pixdata = imag_two.load()
 w,h = imag_two.size
 for y in range(1,h-1):
  for x in range(1,w-1):
   count = 0
   if pixdata[x,y-1] > 245:#上
    count = count + 1
   if pixdata[x,y+1] > 245:#下
    count = count + 1
   if pixdata[x-1,y] > 245:#左
    count = count + 1
   if pixdata[x+1,y] > 245:#右
    count = count + 1
   if pixdata[x-1,y-1] > 245:#左上
    count = count + 1
   if pixdata[x-1,y+1] > 245:#左下
    count = count + 1
   if pixdata[x+1,y-1] > 245:#右上
    count = count + 1
   if pixdata[x+1,y+1] > 245:#右下
    count = count + 1
   if count > 5:
    pixdata[x,y] = 255

 return imag

imag_low = depoint(imag_two)
imag_low.save('low.jpg')
imag_low.show()


print(tesserocr.image_to_text(imag_low))
