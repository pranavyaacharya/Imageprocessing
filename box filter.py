#!/usr/bin/env python
# coding: utf-8

# In[1]:



import cv2
import numpy as np

img = cv2.imread('panda.png')

blur = cv2.blur(img,(5,5))

cv2.imshow('orig.png', img)
cv2.imshow('boxfil.png', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




