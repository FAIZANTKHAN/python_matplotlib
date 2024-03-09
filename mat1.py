import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,42,46]

#plt.plot(x,y) #By this graph is plotted
#plt.plot(x,y, color='green',linewidth=5)#By this you can add color and width of the line
plt.plot(x,y,color='green',linewidth=5,linestyle='dotted')#It is same as previous 2 cases but it can changes the style of the line
plt.xlabel("Day") #It is used to label the x-axis
plt.ylabel("Temperature") #It is used to label the y-axis
plt.title("Weather") #It is used to give the title to the graph
plt.show()  #This is used to show the plotted the graph