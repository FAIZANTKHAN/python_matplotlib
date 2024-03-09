import matplotlib.pyplot as plt
import numpy as np

profit=[40,2,34,12]
company=['Google','Amazon','MicroSoft','FB']
revenue=[90,135,89,27]
xpos=np.arange(len(company))#Create the array that have length of  comapny array
#plt.bar(xpos,revenue)#Create the bar Graph using the xpos(x-axis) and revenue(y-axis)
plt.xticks(xpos,company) #For adding the company name on the x-axis
plt.ylabel("Revenue In Bln")
plt.xlabel("Company Name")
plt.title("US Tech Stocks")
#Let say you want to do another plotting in the same graph
plt.bar(xpos-0.2,revenue,width=0.4,label="Revenue")#Width is used to control the width of the graph and - and + is used for shifting the bar
plt.bar(xpos+0.2,profit,width=0.4,label="Profit")
plt.legend()
plt.show()