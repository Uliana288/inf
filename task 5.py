import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('BTC_data.csv')

fig = plt.figure(figsize = (100,20))
ax1 = fig.add_subplot(111)

x = df['time']
y = df['close']

# Подпишем оси
plt.xlabel('time')
plt.ylabel('Close')

ax1.plot(x,y,'g-', label = 'green dots')
ax1.scatter(x, y, marker='x')
ax1.legend()
ax1.set_title('Bitk')
plt.show()
ax1.grid()

plt.show()