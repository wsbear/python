from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def s():
    a=random.randint(0,255)
    b=random.randint(0,255)
    c=random.randint(0,255)
    return a,b,c

def l():
    a=random.randint(33,127)
    return chr(a)

def k():
    a=random.randint(128,255)
    b=random.randint(128,255)
    c=random.randint(128,255)
    return a,b,c

a=Image.new('RGB',(240,60),(255,0,0))
b=ImageDraw.Draw(a)
c=ImageFont.truetype('arial.ttf',40)
d=ImageFont.truetype('calibri.ttf',40)
e=ImageFont.truetype('impact.ttf',40)
f=ImageFont.truetype('verdana.ttf',40)

for i in range(240):
    for j in range(60):
        b.point((i,j),s())

b.text((10,10),l(),s(),c)
b.text((70,10),l(),s(),d)
b.text((130,10),l(),s(),e)
b.text((200,10),l(),s(),f)

#a=a.filter(ImageFilter.BLUR)

a.save('验证码.jpg')
