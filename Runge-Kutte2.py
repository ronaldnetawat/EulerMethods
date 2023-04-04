# Python Code for the Runge-Kutte 2nd Order Numerical Method, more commonly known as the RK-2

import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
  return y
  
total_time = 1
h = 1/100
n = int(total_time/h)
y = np.zeros((n+1,1))
t = np.zeros((n+1,1))
y[0] = 1
t[0] = 0

for i in range(n):
  s1 = f(t[i], y[i])
  s2 = f(t[i] + h, y[i] + (h*s1))
  y[i+1] = y[i] + h*((s1+s2)/2)
  t[i+1] = t[i] + h;
