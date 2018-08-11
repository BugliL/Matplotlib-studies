import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
from data import matrix

# Data for plotting
w = 10.24
h = 7.68

degrees = [x[0] for x in matrix]

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)

fig, ax = plt.subplots(figsize=(w, h))
lines = [2, 6, 10, 11, 12]
legend = ['Gas loads', 'Crank-pin load', 'Conrod load', 'Tangential force', 'Radial force']
for i,l in enumerate(lines):
    ax.plot(degrees, [x[l] for x in matrix], label=legend[i])

ax.set(xlabel='crank angle (degrees)', ylabel='(daN)',
       title='Gas load, crank-pin and conrod total loads, radial and tangential forces')

# ax.legend(loc='upper center', bbox_to_anchor=(1.4, 0.5), shadow=True, ncol=1)
ax.legend(loc='upper right')
ax.grid()
ax.set_xlim([0,360])

plt.xticks(np.arange(0, 361, 30.0), visible=True)

fig.savefig("test.png")
plt.show()
