import matplotlib.pyplot as plt
blood_sugar=[113,85,90,150,149,88,93,115,80,77,82,129]
#plt.hist(blood_sugar,bins=3,rwidth=0.95) #It will divide the whole plotting into 3 bins(or buckets)
#plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.95,color='yellow') #Whereas it is same as the previous one but it will divide into the given range
blood_sugar_men=[113,85,90,150,149,88,93,115,80,77,82,129]
blood_sugar_women=[67,98.89,120,133,150,84,69,89,79,120,112,100]
plt.hist([blood_sugar_women,blood_sugar_men],bins=[80,100,125,150],rwidth=0.95,color=['pink','blue'],label=['women','men'])
plt.xlabel("Sugar Level")
plt.title("Sugar Analyses")
plt.ylabel("No.of Person")
plt.legend()
plt.savefig("Sugar Level.png",transparent="true",bbox_inches="tight",pad_inches=2)
plt.show()