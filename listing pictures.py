#!/usr/bin/env python
# coding: utf-8

# In[1]:


# listing png images
import os
from os import listdir

# get the path/directory
folder_dir = "C:/pranavya"
for images in os.listdir(folder_dir):

	# check if the image ends with png
    if (images.endswith(".png")):
        print(images)


# In[6]:


# listing all images
import os
from os import listdir

# get the path/directory
folder_dir = "C:/pranavya"
for images in os.listdir(folder_dir):
        print(images)


# In[15]:


#dipaly all images in folder
#import necessary packages 
import cv2 
import os 
import glob 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
 
#Set the path where images are stored 
img_dir = "C:/pranavya" # Enter Directory of all images  
data_path = os.path.join(img_dir,'*') 
files = glob.glob(data_path) 
data = [] 
for f1 in files: 
    img = cv2.imread(f1,0) 
    data.append(img) 
    plt.figure() 
    plt.imshow(img) 


# In[ ]:




