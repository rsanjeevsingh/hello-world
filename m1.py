import matplotlib.pyplot as plt

x=[10,20,30,40,50]
y=[100,200,300,400,500]

x1=[100,200,300,400,500]
y1=[10,20,30,40,50]

plt.plot(x,y,label="Line 1")
plt.plot(x1,y1,label="Line 2")

plt.xlabel('X- Co-ordinate values')
plt.ylabel('Y- Co-ordinate values')
plt.title('TItile - Sample Visualization Chart')
plt.style.use('tableau-colorblind10')
plt.legend()
plt.show()
