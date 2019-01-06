import matplotlib.pyplot as plt


days=[1,2,3,4,5]
sleep=[80,8,8,8,8]
eating=[10,1,12,1,2]
working=[10,10,10,10,10]
playing=[10.5,1,1,0.7,5]
#Workaround for Legend..
plt.plot([],[], color='c',label='Sleeping',linewidth=5)
plt.stackplot(days,sleep,eating,working,playing,colors=['c','y','b','r','g'])

plt.xlabel('x-label')
plt.ylabel('y-label')

plt.legend()
plt.title('Sample Stack Plot')

plt.show()
