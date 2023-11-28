import numpy as np
import matplotlib.pyplot as plt
labels = ['Ireland','Iceland','South Korea','Germany','US','Italy']
values = [17.7,10.7,10.2,10.2,21,30.3]
colors = ['#be5168','#e16552','#e2975d','#e9d78e','#3c8e9d','#993767']
plt.pie(values,colors=colors,autopct='%1.1f%%',wedgeprops = {"edgecolor" : "white",'linewidth': 1,'antialiased': True},startangle=145,textprops={'color':"w"})
plt.legend(labels,loc ="center left",bbox_to_anchor =(0.83, 0.5, 0, 0))
plt.axis('equal')
plt.show()