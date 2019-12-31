import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
plt.rcParams['axes.unicode_minus'] = False    # 设置显示负号
plt.rcParams["font.sans-serif"]='SimHei'  #解决中文乱码问题
x=np.array([1,2,3,4,5,6,7,8,9])
y1=np.array([866,2335,5710,6483,6120,1590,2349,4438,4590])
y2=np.array([0.866,0.2335,0.5710,0.6483,0.6120,0.1590,0.2349,0.4438,0.4590])

fig, ax1 = plt.subplots()

ax1.bar(x,y1,label="注册量",color="steelblue")
ax1.set_xlabel('月份')
ax1.set_xlim(0, 10)
ax1.set_xticks(range(11))
ax1.set_ylabel("注册量", color='blue')
ax1.legend(loc="upper left")
ax1.set_ylim(0, 8000)
ax1.set_yticks(range(0, 8001, 800))
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.tick_params(axis='y', which='major', colors='blue', direction='in')
#数据标签
for a,b in zip(x,y1):
     plt.text(a,b,b,ha='center',va="bottom",fontsize=11)

ax2 = ax1.twinx()
ax2.plot(x, y2,label="激活率", color="red",linestyle="solid",linewidth=1,marker="o",markersize=3)
ax2.legend()
ax2.set_ylabel("激活率", color="red")
ax2.set_ylim(0, 1)
ax2.tick_params(axis='y', colors='red', direction='inout')  #设置刻度线

plt.title("1-9月注册与激活率",loc="center")
plt.show()
plt.savefig(r"C:\Users\CQ375\Desktop\ex\twinx.png")