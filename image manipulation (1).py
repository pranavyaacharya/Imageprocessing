#!/usr/bin/env python
# coding: utf-8

# In[8]:


#image sharpness
from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt

image=Image.open("images 2.jpg")
sharp=image.filter(ImageFilter.SHARPEN)
sharp.save("D:\IP\sharper.jpg")
sharp.show()
plt.imshow(sharp)
plt.show()


# In[10]:


#image flip
import matplotlib.pyplot as plt
image=Image.open("images 2.jpg")
plt.imshow(image)
plt.show()
flip=image.transpose(Image.FLIP_LEFT_RIGHT)

flip.save("D:/IP/flip.jpg")
plt.imshow(flip)
plt.show()


# In[40]:


#cropping
#image sharpness
from PIL import Image
import matplotlib.pyplot as plt
image=Image.open("images 2.jpg")
width,height=image.size
im1=image.crop((50,50,200,200))
im1.show()
plt.imshow(im1)
plt.show()


# In[ ]:




