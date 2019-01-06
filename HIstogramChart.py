import matplotlib.pyplot as plt

population=[100,200,300,400,500]
bins=[60,70,80,90,100]

plt.hist(population,bins,histtype='bar',rwidth=0.5)

plt.xlabel('x-label')
plt.ylabel('y-label')
plt.bar(population,bins)
plt.show()
