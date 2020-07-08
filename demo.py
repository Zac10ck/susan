# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:41:20 2020

@author: ASUS
"""

# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 




# potting the points 



plt.plot([0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.5, 1.7, 1.8], [0.75,1.25, 1.45, 1.25, 0.85, 0.55, 0.35, 0.28, 0.18])
plt.xlabel('x Label')
plt.ylabel('y Label')
plt.title('nonlinear fit')

plt.legend()

# function to show the plot 
plt.show() 
