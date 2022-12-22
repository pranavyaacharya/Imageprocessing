#!/usr/bin/env python
# coding: utf-8

# In[1]:


#converting format
from PIL import Image
image=Image.open("buny.jpg")

image.save("double heart.png")
print("successfully converted")


# In[2]:


#print mode
print(image.mode)


# In[3]:


#crop image
import cv2

img=cv2.imread("images7.jpg")
crop=img[50:200, 100:400]
cv2.imshow("Original image",img)
cv2.imshow("Cropped image",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


#negating image
im = Image.open("image10.jpg") 
im_t = im.point(lambda x: 255 - x)
im_t.show()


# In[5]:


#separting RGB channels

from skimage.io import imread,imshow
import matplotlib.pyplot as plt
img = imread("images1.jpg")
imshow(img)

fig,ax=plt.subplots(1,3,figsize=(12,4),sharey=True)
ax[0].imshow(img[:,:,0],cmap="Reds")
ax[0].set_title("Red")
ax[1].imshow(img[:,:,1],cmap="Greens")
ax[1].set_title("Green")
ax[2].imshow(img[:,:,2],cmap="Blues")
ax[2].set_title("Blue")


# In[16]:


#histogram
import matplotlib.pyplot as plt
im=Image.open("images1.jpg")
pl=im.histogram()
plt.bar(range(256),pl[:256],color="r",alpha=0.5)
plt.bar(range(256),pl[256:2*256],color="g",alpha=0.4)
plt.bar(range(256),pl[2*256:],color="b",alpha=0.3)
plt.show()


# In[19]:


#texton an image
from PIL import Image, ImageDraw,ImageFont
image=Image.open("images3.jpg")
draw=ImageDraw.Draw(image)
font=ImageFont.truetype("ALGER.TTF",30)
draw.text((50,60),"hello",font=font,fill=(0,0,0))

image.show()


# In[17]:


#Image blending

im1=Image.open("buny.jpg")
im2=Image.open("doggy.jpg")

alpha1=Image.blend(im1,im2,alpha=.4)
alpha2=Image.blend(im1,im2,alpha=.4)

alpha1.show()
alpha2.show()


# In[9]:


#statistics on image
from PIL import Image, ImageStat
image=Image.open("images3.jpg")
stat=ImageStat.Stat(image)
print(stat.mean)
print(stat.median)
print(stat.stddev)


# In[ ]:




