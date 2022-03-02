# Degradation of Data Integrity
# Brett Silvey & Paul Andrews

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Define the ODE  x(t) = e^1/20t
def function(t):
    return np.exp((-1/20)t)

ts = []  # create an empty list to store the time values
xs = []  # create an empty list to store the x values

ts = np.linspace(0,100,1000)  # create a list of 1000 time values between 0 and 100
for t in ts:  # for each time value in the list
    xs.append(function(t))  # append the value of x to the list of x values

plt.title("Degradation of Data Integrity")
plt.xlabel("t")
plt.ylabel("x")
plt.plot(ts, xs, 'b-', linewidth=2)  # plot the x values against the time values
plt.show()
