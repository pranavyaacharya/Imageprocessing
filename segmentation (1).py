#!/usr/bin/env python
# coding: utf-8

# In[1]:


from skimage.segmentation import slic
from skimage.color import label2rgb
import matplotlib.pyplot as plt

face_image=plt.imread("face.jpg")

#obtain the segmentation with 400 regions
segments=slic(face_image,n_segments=400)
    
#put segments on top of origibal image to compare
segmented_image=label2rgb(segments,face_image,kind='avg')

#show the original
plt.title("original")
plt.imshow(face_image.astype('uint8'))
plt.show()

#show noisy image
plt.title("segemented image")
plt.imshow(segmented_image.astype('uint8'))
plt.show()
 


# In[ ]:




