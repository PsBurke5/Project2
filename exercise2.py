import numpy as np
import matplotlib.pyplot as plt
import scipy
import fitting_functions
from scipy.stats import norm

data = np.loadtxt("data2.csv", delimiter=",", dtype=str)

print(data[0])

d = data[1:, 0].astype(np.float32)
f = data[1:, 1].astype(np.float32)

print(d)
print(f)

params, params_cov = scipy.optimize.curve_fit(fitting_functions.linear, d, f)
slope = params[0]
intercept = params[1]

fitting_functions.print_equation(slope, intercept, 'N', 'm')
fig = plt.figure()
plt.scatter(d, f, label='Data')
plt.plot(d, fitting_functions.linear(slope, d, intercept), label='Linear Fit')
plt.legend(loc='best')
plt.xlabel("Displacement (m)")
plt.ylabel("Force (N)")
plt.show()
fig.savefig("plot_spring2.png")


'''
Exercise 1 equation:
F = 200d - 0.000000357

Exercise 2 equation:
F = 100d - 0.000000366

Similarities:
Both equations are linear, and both have y-intercepts
that are very close to zero.

Differences:
The slope of the first equation is approximately 200 N/m,
while the slope of the second equation is approximately
100 N/m. This means the first spring is twice as stiff
as the second spring.
'''
