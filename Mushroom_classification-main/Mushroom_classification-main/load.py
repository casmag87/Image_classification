#!/usr/bin/env python
# coding: utf-8

# In[74]:


import splitfolders as sf
import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt

# In[ ]:
class_names = ['Boletus','Entoloma','Russula','Suillus','Lactarius','Amanita','Agaricus','Hygrocybe','Cortinarius']
class_names_label = {class_name:i for i, class_name in enumerate(class_names)}










# In[75]:


def split_data():
        inputfolder = "./mushrooms-classification-common-genuss-images/mushrooms/"
        sf.ratio(inputfolder, output="./Mushrooms/Mushrooms_data",
        seed=1000, ratio = (.8, .1, .1), 
        group_prefix=None)


# In[76]:




# In[77]:


def load_data():
    DIRECTORY = "./Mushrooms/Mushrooms_data"
    CATEGORY = ["train","test"]
    IMAGE_SIZE = (32,32)

    output = []
    
    for category in CATEGORY:
        path = os.path.join(DIRECTORY,category)
       
        
        images = []
        labels = []
        
        print("loading{}".format(category))
        print(path)
        print(os.listdir(path))
        for folder in os.listdir(path):
            try:
                label = class_names_label[folder]
            except KeyError as e: 
                print(type(e), e)
            for file in os.listdir(os.path.join(path, folder)):
                
                img_path = os.path.join(os.path.join(path, folder), file)
                
                image = cv2.imread(img_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = cv2.resize(image, IMAGE_SIZE)
                
                images.append(image)
                labels.append(label)
                
        images = np.array(images, dtype = 'float64')
        labels = np.array(labels, dtype = 'uint8')
        
        output.append((images, labels))

    
    
    return output

    


# In[ ]:
def plot_sample(x, y, index):
    plt.figure(figsize = (15,2))
    plt.imshow(x[index].astype('uint8'))
    plt.xlabel(class_names[y[index]])


  






