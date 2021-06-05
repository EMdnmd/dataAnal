'''
模板介绍：
coding: utf-8
Team : 无
Author：张恒瑞
Date ：2021/5/31 9:45
Tool ：PyCharm
'''
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
from  matplotlib import  pyplot as plt
im=Image.open("hd.jpg")
print(im)
mask=np.array(im)
f=open("tjaq.py",'r',encoding='utf-8')
text=f.read()
wc = WordCloud(background_color="white",max_words=200,max_font_size=80,mask=mask).generate(text)
wc.to_file('asd.jpg')
image_colors = ImageColorGenerator(mask)

plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.show()
