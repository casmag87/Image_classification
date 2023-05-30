#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tensorflow import keras
from keras.models import Sequential
import numpy as np
import load as ld
import matplotlib.pyplot as plt
from skimage.transform import resize


# In[ ]:


cnn = keras.models.load_model('model')


# In[ ]:


print("insert picture")
image = input("")
new_image = plt.imread(image)
resized_image = resize(new_image, (32,32,3))
img = plt.imshow(resized_image)


# In[ ]:


predictions = cnn.predict(np.array([resized_image]))


# In[ ]:


print('Array\n', predictions)


# In[ ]:


list_index = [0,1,2,3,4,5,6,7,8]
x = predictions
classification = ['Boletus','Entoloma','Russula','Suillus','Lactarius','Amanita','Agaricus','Hygrocybe','Cortinarius']

for i in range(len(list_index)):
      
    
   
    for j in range(len(list_index)):
        if x[0][list_index[i]] > x[0][list_index[j]]:
            temp = list_index[i]
            list_index[i] = list_index[j]
            list_index[j] = temp


print('\n top 5 bud på mushrooms')
for i in range(5):
    print(classification[list_index[i]], ':', round(x[0][list_index[i]] * 100, 2), '%')


# In[ ]:




