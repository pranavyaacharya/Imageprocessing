#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import skimage.io
import skimage.util

a = skimage.io.imread('image9.jpg')
#print(a.shape)
# (225, 400, 3)

b = a // 2
c = a // 3

m = skimage.util.montage([a, b, c], multichannel=True)
#print(m.shape)
# (450, 800, 3)

cv2.imshow('to display images',m)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




