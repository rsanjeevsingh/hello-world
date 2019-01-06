import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

#Date COnversion

c1,c2,c3,c4,c5,c6,c7,c8=np.loadtxt('NSE-Wipro.csv', delimiter=',',unpack=True, skiprows=1,
                                   converters={0: mdates.strpdate2num('%Y-%m-%d')})


plt.plot_date(x=c1,y=c2,fmt='.')

plt.xlabel('Date')
plt.ylabel('Price')

plt.legend()

plt.title("Wipro Share Price")

plt.show()
