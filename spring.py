import numpy as np
import matplotlib.pyplot as plt
import scipy
import fitting_functions
from scipy.stats import norm

data = np.loadtxt("data.csv", delimiter=",", dtype=str)

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
fig.savefig("plot_spring.png")
