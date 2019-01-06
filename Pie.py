import matplotlib.pyplot as plt


slices=[8,2,10,4]
activity=['sleep','eating', 'working','playing']
c=['c','m','r','b']
#8%24 hours pie chart does with slices

plt.pie(slices,labels=activity,colors=c,startangle=0,explode=(0,0.2,0,0),autopct='%1.1f%%',shadow=True)

plt.title('Sample Pie Plot')

plt.show()
