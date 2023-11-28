import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x =[]
for i in range(1,61):
    i = i+2
    if i%2 != 0:
        x.append(i)
fig.suptitle("This is the Title")#,fontsize = 20
plt.xlabel('This is the X axis')
plt.ylabel('This is the Y axis')
y = [45,48,64,67,66,8,83,20,35,87,70,87,86,13,57,65,38,87,45,87,80,38,25,76,72,9,20,80,70,79]
val = [13,16,22,1,4,28,4,8,10,20,22,19,5,24,7,25,25,13,27,2,7,8,24,15,25,18,6,26,14,9]
ax.plot(x,y)
plt.xticks (ticks=x, labels=val,c='red')
ax.set_facecolor('#eaeaf2')
ax.grid(c="white")
ax.scatter(x,y,marker = '^')
plt.show()