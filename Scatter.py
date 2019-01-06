import matplotlib.pyplot as plt

population=[1,2,3,4,5,6,7,8,9]
bins=[6,3,2,1,4,5,8,9,7]

plt.scatter(population,bins,label='Scatter',color='R',marker="4")

plt.xlabel('x-label')
plt.ylabel('y-label')
plt.legend()
plt.show()
