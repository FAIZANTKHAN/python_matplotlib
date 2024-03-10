import matplotlib.pyplot as plt
import numpy as np
#Plot a bar chart that looks like below
#Save this chart as jpg file and then pdf file with 5 inch of padding
company=['GOOGL','AMZN','MSFT','FB']
revenue=[90,136,89,27]
xpos=np.arange(len(company))
plt.xticks(xpos,company)
plt.xlabel("Comapany")
plt.title("US Tech Stocks")
plt.ylabel("Revenue(BlN)")
plt.bar(xpos,revenue)
plt.savefig("Usstocks.jpg" ,bbox_inches="tight")#Saving it in format of jpg
plt.savefig("Usstocks.pdf",bbox_inches="tight",pad_inches=5)#Saving in the format of  pdf with padding of 5 inches
plt.show()