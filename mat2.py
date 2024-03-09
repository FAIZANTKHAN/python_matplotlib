import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,42,46]

#plt.plot(x,y,'r+')  #It is "r+" shortcut which is representing red colour line wich '+' sign on the spot.
#plt.plot(x,y, color="red",linestyle=" ",marker="+")#For representing in full
#You can  also change the size of marker using "markersize"

plt.plot(x,y,color='green',linestyle='--',marker='+',markersize='0.2',alpha=0.2)#Using all the above thing

plt.show()