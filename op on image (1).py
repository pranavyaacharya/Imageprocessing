#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


image=cv2.imread("images6.jpg")
cv2.imshow("to display image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[3]:


cv2.imwrite("C:\pranavya\image9.png",image)


# In[4]:


#loading from external drive
image=cv2.imread("C:\pranavya\images (2).jpg")
cv2.imshow("to display image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


#greyscale
image=cv2.imread("images6.jpg",0)
cv2.imshow("to display image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


#height and width
from PIL import Image

x="images.jpg"
img=Image.open(x)

width=img.width
height=img.height

print("The height of the image is",height)
print("The weight of the image is",width)


# In[7]:


#no of cannels from color-image

import numpy

img=cv2.imread("images1.jpg")
print("No of channels is:"+str(img.ndim))
print("No of channels is:",img.shape)
cv2.imshow("channel",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


#Resize image

from PIL import Image
filepath="images7.jpg"
im=Image.open(filepath)
new_im=im.resize((400,400))
new_im


# In[9]:


#no of cannels from greayscale image

import numpy

img=cv2.imread("images1.jpg",0)
print("No of channels is:"+str(img.ndim))
print("No of channels is:",img.shape)
cv2.imshow("channel",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[10]:


#matrix repsresentation of image

import matplotlib.image as image
img=image.imread("image10.jpg")
print("The shape of the image is",img.shape)
print("The array of image is")
print(img)


# In[11]:


#binary image

import cv2
img=cv2.imread("images 2.jpg")
ret,bw_img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#converting to its binary form
bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow("BINARY",bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[12]:


import cv2
img=cv2.imread("images7.jpg")
B,G,R=cv2.split(img)
print(B)
print(G)
print(R)


# In[13]:



cv2.imshow("BLUE",B)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[14]:



cv2.imshow("RED",R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[15]:


img=cv2.imread("images 2.jpg")
cv2.imshow("GREEN",G)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[16]:


#Aspect ratio

img=cv2.imread("images 2.jpg")
new_im=img.resize((400,200))
ar=1*(img.shape[1]/img.shape[0])
print("asepect ratio")
print(ar)


# In[17]:


#different color spaces
import cv2
img=cv2.imread("image10.jpg")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
hls=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
yuv=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

cv2.imshow("GREY",grey)
cv2.imshow("HSV",hsv)
cv2.imshow("LAB",lab)
cv2.imshow("HLS",hls)
cv2.imshow("YUV",yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[18]:


#miror image
from PIL import Image
filepath="image9.jpg"
img=Image.open(filepath)
hori_flippedImage=img.transpose(Image.FLIP_LEFT_RIGHT)
img.show()
hori_flippedImage.show()

#vertical
vert_flippedImage=img.transpose(Image.FLIP_TOP_BOTTOM)
vert_flippedImage.show()


# In[ ]:


import cv2
img1=cv2.imread("buny.jpg")
img2=cv2.imread("doggy.jpg")
sum=img1+img2
sub=img1-img2
mul=img1*img2
div=img1/img2
cv2.imshow("sum:",sum)
cv2.imshow("sub:",sub)
cv2.imshow("mul:",mul)
cv2.imshow("div:",div)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




