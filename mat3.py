import matplotlib.pyplot as plt

#Multiple Plotting in Same Graph
days=[1,2,3,4,5,6,7]
max_t=[50,51,52,48,47,49,46]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,43,46,40,42,41]

plt.title("Temperature Report")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.plot(days,max_t,label="Max")
plt.plot(days,min_t,label="Min")
plt.plot(days,avg_t,label="Avg")
plt.legend()

plt.show()