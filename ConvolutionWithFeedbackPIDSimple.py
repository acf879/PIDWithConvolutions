#!/usr/bin/env python
# coding: utf-8

# In[2062]:


import random as rn # samples for simple H(z) = P(z) + I(z) + D(z) configuration
import numpy as np


# In[2063]:


MAX = 10 # Max for samples


# In[2064]:


MIN = -10 # Min for samples


# In[2065]:


x_input = [(MAX-MIN)*rn.random() + MIN for x in range(10)] # Get lin. distrib. rand. nums to act as sample


# In[2066]:


T = 1e-6 # Time step


# In[2067]:


ki = 0.5 # integration parameter


# In[2068]:


kd = 0 # derivative parameter


# In[2069]:


kp = 100 # pass parameter


# In[2070]:


h_p = [T*ki/2 + 2*kd/T + kp, T*ki - 4*kd/T, T*ki/2 + 2*kd/T - 1] # transfer function without feedback


# In[2071]:


g = [2] # feedback term


# In[2072]:


def convolution_with_feedback(x ,first_indx_x, h, first_indx_h, g, first_indx_g):
    # Initialize variables
    len_y = len(x) + len(h)
    len_x = len(x)
    y_feed_val = 0
    x_indx = 0
    
    H = np.zeros((len(h) + first_indx_h, 1))
    G = np.zeros((len(g) + first_indx_g,1))
    y = np.zeros((len_y,1))
    X = np.zeros((len_y,1))
    
    for i in range(len(g)):
        G[i+first_indx_g] = g[i]
        
    for i in range(len(h)):
        H[i+first_indx_h] = h[i]
    
    for i in range(0,len(x)):
        X[i+first_indx_x] = x[i]
    
    G = np.flip(G)
    H = np.flip(H)  
    
    first_indx_y = first_indx_x + first_indx_h
    y_indx = first_indx_y
    

    # Calculate
    for i in range(0, len_y-1):    
        if (y_indx > first_indx_y):
            
            y_feed = y[i-1] 
            for j in range(0,len(G)):
                y_feed_val += y_feed*G[j]        
        for j in range(0,len(H)):
            y[i] += X[j+x_indx]*H[j]  
        y[i] += y_feed_val
        y_feed_val = 0
        
        if x_indx < len(x):
            x_indx += 1
        y_indx += 1
        
    return (first_indx_y, y[:-1])


# In[2073]:


x0=[1,2,3,4,0,0,0,0,0,0]


# In[2074]:


h0=[1/2,1/2]


# In[2075]:


x_indx=1


# In[2076]:


h_indx=0


# In[2077]:


g0=[1]


# In[2078]:


g_indx = 1


# In[2079]:


convolution_with_feedback(x0 ,x_indx, h0, h_indx, g0, g_indx) # produces expected output when done by hand


# In[2080]:


convolution_with_feedback(x_input, 0, h_p, 0, g, 2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




