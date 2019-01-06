import matplotlib.pyplot as plt

x=[10,20,30,40,50]
y=[20,30,40,50,60]

x1=[15,25,35,45,55]
y1=[30,40,50,60,70]

plt.plot(x,y,label="Line 1",color='G')
plt.bar(x,y,label="Bar 1",color="#001100")
plt.bar(x1,y1,label="Bar 2")

plt.xlabel('X- Co-ordinate values')
plt.ylabel('Y- Co-ordinate values')
plt.title('TItile - Sample Visualization Bar Chart')
plt.style.use('tableau-colorblind10')
plt.legend()
plt.show()
