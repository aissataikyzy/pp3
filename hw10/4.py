import numpy as np
import matplotlib.pyplot as plt
labels = ['UK','US','South Korea','Australia','Germany','India']
values = [24.6,18.25,9.2,3.2,16.5,27.7]
colors = ['green','blue','yellow','purple','#22b4cd','red']
explode = [0,0.1,0,0,0,0]
plt.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180)
plt.axis('equal')
plt.show()