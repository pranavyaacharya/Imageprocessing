#!/usr/bin/env python
# coding: utf-8

# In[1]:


#CANNY EDGE DETECTION
import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# In[2]:


loaded_image=cv2.imread("pooki.jpg")
loaded_image=cv2.cvtColor(loaded_image,cv2.COLOR_BGR2RGB)


# In[3]:


gray_image=cv2.cvtColor(loaded_image,cv2.COLOR_BGR2GRAY)


# In[4]:


edge_image=cv2.Canny(gray_image,threshold1=65,threshold2=500)


# In[5]:


plt.figure(figsize=(20,20))
plt.subplot(1,3,1)
plt.imshow(loaded_image,cmap="gray")
plt.title("original image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(gray_image,cmap="gray")
plt.title("grascale image")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(edge_image,cmap="gray")
plt.title("canny edge detected image")
plt.axis("off")
plt.show()


# In[6]:


#LAPLACIAN AND SOBEL EDGE DETCTION
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("sun.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.GaussianBlur(gray,(3,3),0)


# In[7]:


laplacian=cv2.Laplacian(img,cv2.CV_64F)
soblex=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobley=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)


# In[8]:


plt.subplot(2,2,1)
plt.imshow(img,cmap="gray")
plt.title("original")
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(laplacian,cmap="gray")
plt.title("Laplacian")
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(soblex,cmap="gray")
plt.title("sobel x")
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(sobley,cmap="gray")
plt.title("sobel y")
plt.xticks([])
plt.yticks([])

plt.show()


# In[29]:


#EDGE DETCETION  USING PREWITT OPERATOR
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("ChessBoardGrad.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_guassian=cv2.GaussianBlur(gray,(3,3),0)


# In[30]:


kernelx=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx=cv2.filter2D(img_guassian,-1,kernelx)
img_prewitty=cv2.filter2D(img_guassian,-1,kernely)


# In[31]:


cv2.imshow("original image",img)
cv2.imshow("prewitt x",img_prewittx)
cv2.imshow("prewitt y",img_prewitty)
cv2.imshow("prewitt ",img_prewittx+img_prewitty)
cv2.waitKey()
cv2.destroyAllWindows()


# In[65]:


#ROBORTS EDGE DETECTION
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

roberts_cross_v=np.array([[1,0],
                         [0,-1]])

roberts_cross_h=np.array([[0,1],
                         [-1,0]])

img=cv2.imread("panda.png",0) .astype('float64')
img/=255.0
vertical=ndimage.convolve(img,roberts_cross_v)
horizontal=ndimage.convolve(img,roberts_cross_h)

edge_image=np.sqrt(np.square(horizontal)+ np.square(vertical))
edge_image*=255
cv2.imwrite("op.jpg",edge_image)
cv2.imshow("outputimage",edge_image)
cv2.waitKey()
cv2.destroyAllWindows()


# In[61]:





# In[ ]:





# In[40]:





# In[ ]:




