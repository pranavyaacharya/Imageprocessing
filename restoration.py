#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import cv2
 
# Open the image.
img = cv2.imread('cat_damaged.jpg')
 
# Load the mask.
mask = cv2.imread('cat_mask.jpg', 0)
 
# Inpaint.
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
 
# Write the output.
cv2.imshow('to display images',img)
cv2.imshow('to display images',mask)
cv2.imshow('to display images',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




