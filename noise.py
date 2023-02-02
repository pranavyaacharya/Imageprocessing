#!/usr/bin/env python
# coding: utf-8

# Adding noise

# In[12]:


from skimage.util import random_noise
import matplotlib.pyplot as plt
fruit_image = plt.imread('sun.jpg')

#add noise
noisy_image=random_noise(fruit_image)

#show the original
plt.title("original")
plt.imshow(fruit_image)
plt.show()

#show noisy image
plt.title("noisy image")
plt.imshow(noisy_image)
plt.show()
 


# REDUCING NOISE

# In[15]:


from skimage.restoration import denoise_tv_chambolle
import matplotlib.pyplot as plt

noisy_image=plt.imread("npoise.jpg")

#apply total variatin filter denoising
de_img=denoise_tv_chambolle(noisy_image,multichannel=True)

#show the original
plt.title("noisy image")
plt.imshow(noisy_image)
plt.show()

#show denoised image
plt.title("denoised image")
plt.imshow(de_img)
plt.show()
 


# In[ ]:


REDUCING WHILE PRESEVRVING EDGES


# In[16]:


from skimage.restoration import denoise_bilateral

landscape_image=plt.imread("npoise.jpg")

#applybilateral filter
de_img=denoise_bilateral(landscape_image,multichannel=True)

#show the original
plt.title("noisy image")
plt.imshow(landscape_image)
plt.show()

#show noisy image
plt.title("denoised image")
plt.imshow(de_img)
plt.show()
 


# In[ ]:




