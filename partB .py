# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:54:00 2020

@author: Susan
"""

import matplotlib.pyplot as plt

def found_fit(x):
    #return 0.388 * x**2  # Found with symfit.

x_data =  [0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.5, 1.7, 1.8]

y_data = [0.75,1.25, 1.45, 1.25, 0.85, 0.55, 0.35, 0.28, 0.18]




# x  0.1 0.2 0.4 0.6 0.9 1.3 1.5 1.7 1.8
# y  0.75 1.25 1.45 1.25 0.85 0.55 0.35 0.28 0.18


#x_func = np.linspace(0, 10, 50)
# numpy will do the right thing and evaluate found_fit for all elements
#
# From here the plotting starts

#plt.scatter(x_data, y_data, c='r', label='data')
plt.plot(x_func, y_func)
plt.xlabel('x  Axis')
plt.ylabel('y Axis')
plt.title('nonlinear fit')
plt.legend()
plt.show()