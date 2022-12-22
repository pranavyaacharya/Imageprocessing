#!/usr/bin/env python
# coding: utf-8

# In[29]:


#upsamapling
import cv2

image=cv2.imread("images 4.jpg")
cv2.imshow("before",image)

image=cv2.pyrUp(image)
cv2.imshow("after",image)
cv2.waitKey()
cv2.destroyAllWindows()


# In[49]:


#downsamapling
import cv2
from matplotlib  import pyplot as plt
image=cv2.imread("images 4.jpg")
cv2.imshow("before",image)

image=cv2.pyrDown(image)
plt.imshow(image)
cv2.imshow("after",image)
cv2.waitKey()
cv2.destroyAllWindows()


# In[34]:


#nearest interplation
import cv2
import numpy as np

img = cv2.imread('p.jpg')
near_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_NEAREST)
cv2.imshow('Near',near_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[37]:


#linear interpolation
import cv2
import numpy as np
img = cv2.imread('p.jpg')
bilinear_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_LINEAR)
cv2.imshow('Bilinear',bilinear_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# In[39]:


#cubic interpolation
import cv2
import numpy as np

img = cv2.imread('p.jpg')
bicubic_img = cv2.resize(img,None, fx = 5, fy = 5, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Bicubic',bicubic_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[45]:


# Quantization
from PIL import Image 
import PIL 
im1 = Image.open("buny.jpg") 
im1 = im1.quantize(16) 
im1.show() 


# In[ ]:




