#!/usr/bin/env python
# coding: utf-8

# In[12]:


import cv2
import numpy as np
img=cv2.imread("mark.jpg")
cv2.imshow("orginal",img)

alpha=2.0
beta=-160

new=alpha*img+beta
new=np.clip(new,0,255).astype(np.uint8)

cv2.imshow("to dislay image",new)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




