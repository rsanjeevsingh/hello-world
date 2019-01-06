import matplotlib.pyplot as plt
import numpy as np

c1,c2=np.loadtxt('NSE-Wipro.csv',delimiter=',',unpack=True,skiprows=1,usecols=(2,3))

print c1,c2

plt.bar(c1,c2,label='loaded from numpy')

plt.xlabel('X-Label Here')
plt.ylabel('Y-Label Here')

plt.legend()

plt.title("Sample data plot from file")

plt.show()
