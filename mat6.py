import matplotlib.pyplot as plt
exp_vals=[1400,600,300,410,250]
exp_labels=["Home Rent","Food","Phone/Internet Bill","Car","Other Utilities"]
#plt.pie(exp_vals,labels=exp_labels)#Here we are plotting the pie chart on the basis of exp_vals and labeling the data with the exp_labels
plt.axis('Equal')
plt.pie(exp_vals,labels=exp_labels,radius=1.5,autopct='%0.f%%')#radius will control the radius and autopct will add extra to  the output like in this case it will add the percentage of expenses
plt.savefig("expense.png",bbox_inches="tight",pad_inches=2)#for saving the picture of graph
#bbox_inches is used for download the whole pic is captured whereas pad_inches used for adding padding to the pic
#You use transparent as well download the picture in any format
plt.show()
