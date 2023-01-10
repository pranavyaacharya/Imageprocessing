#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import module
from PIL import Image, ImageChops
import matplotlib.pyplot as plt
  
# assign images
img1 = Image.open("1img.jpg")
plt.imshow(img1)
plt.show()

img2 = Image.open("2img.jpg")
plt.imshow(img2)
plt.show()

# finding difference
diff = ImageChops.difference(img1, img2)
  
# showing the difference
plt.imshow(diff)
plt.show()


# In[ ]:




