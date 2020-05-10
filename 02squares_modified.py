"""import matplotlib.pyplot as plt
squares=[1,4,9,16,25]
plt.plot(squares,linewidth=4) #plots number with line width 14
plt.title("SQUARE NUMBER",fontsize=24) #title is given
plt.xlabel("Value",fontsize=15) #x axis value 
plt.ylabel("Squares of the value",fontsize=15) #y axis value
plt.tick_params(axis="both",labelsize=12)#increases the unit font size
#set size of the tick labels
plt.show()"""

import matplotlib.pyplot as plt
cubes=[1,8,27,64,125]
plt.plot(cubes,linewidth=11)
plt.title("Cube of the numbers",fontsize=23)
plt.xlabel("X-value",fontsize=11)
plt.ylabel("Y-value",fontsize=11)
plt.tick_params(axis="both",labelsize=12)
plt.show()
