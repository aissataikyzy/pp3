import matplotlib.pyplot as plt
import numpy as np

y = np.array([30.3, 21, 10.2, 10.2, 10.7, 17.7, 3.6, 3.8, 4.1, 4.2, 5.3])

labels = ["Italy", "Spain", "Germany", "Greece", "Iceland", "Ireland", "Austria", "Belgium", "Denmark", "Finland", "France" ]
plt.title("Countries")

colors = ["MediumVioletRed", "DarkCyan", "DarkOliveGreen", "GoldenRod", "Ivory", "LightCoral", "MediumOrchid", "MediumSeaGreen", "MistyRose", "PLum", "LemonChiffon"]

plt.pie(y, colors=colors, autopct="%.1f%%", textprops=dict(fontsize=8))
plt.legend(labels=labels, loc='upper center',
           bbox_to_anchor=(0.5, 0.05), ncol=5 )
plt.show()
