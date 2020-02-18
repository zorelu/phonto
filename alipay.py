from PIL import Image, ImageDraw, ImageFont
import time

image = Image.open('./img/try.jpg')
draw = ImageDraw.Draw(image)
font1=ImageFont.truetype('./ttf/huawei.otf',100)
#price
draw.rectangle((440,660,670,385),(255,255,255))
#stime
draw.rectangle((680,1000,1040,940),(255,255,255))
draw.text((435,360),'16.00',(0,0,0), font=font1)
font2=ImageFont.truetype('./ttf/huawei.otf',45)
daytime="2020-02-28"
nowtime="09:25"
datime=daytime + " "  + nowtime
draw.text((685,946),datime,(48,48,48), font=font2)
image.show()
image.save('./img/try2.jpg', 'jpeg')