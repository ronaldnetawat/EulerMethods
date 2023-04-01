import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
R1, Q1 = 0.3, 10
R2, Q2 = 0.4, 10

# Define the time interval and step size
total_time = 20
h = 1/100
n = int(total_time/h)

# Set up the arrays to store the solutions
y1 = np.zeros((n+1, len([1,1.5,2,2.5,3,3.5,4,4.5,5])))
y2 = np.zeros((n+1, len([1,1.5,2,2.5,3,3.5,4,4.5,5])))
t = np.zeros((n+1,))

# Set the initial conditions for each solution
for i, y0 in enumerate([1,1.5,2,2.5,3,3.5,4,4.5,5]):
    y1[0,i], y2[0,i] = y0, y0
    
# Compute the solutions for each initial condition for the two sets of parameters
for i in range(n):
    for j, y0 in enumerate([1,1.5,2,2.5,3,3.5,4,4.5,5]):
        y1[i+1,j] = y1[i,j] + h*f(t[i], y1[i,j], R1, Q1)
        y2[i+1,j] = y2[i,j] + h*f(t[i], y2[i,j], R2, Q2)
    t[i+1] = t[i] + h
    
 
# Plot the solutions
fig, ax = plt.subplots()
ax.plot(t, y1, label=f'R={R1}, Q={Q1}')
ax.plot(t, y2, label=f'R={R2}, Q={Q2}')
#ax.legend()
ax.set_xlabel('Time')
ax.set_ylabel('y')
plt.show()
