# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:41:32 2021

@author: Leandro
"""

import numpy as np
import scipy as sc

from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
x= np.array([-1,1,2])
y= np.array([-3,3,9])
poly= lagrange(x,y)

Polynomial(poly).coef
