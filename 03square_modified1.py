"""In the previous chart it was not specific . At the end of the graph square of 4.0 is shown as 25, lets fix it"""

import matplotlib.pyplot as plt
input_value=[1,2,3,4,5]  #input value
squares=[1,4,9,16,25]  #square of the value
plt.plot(input_value,squares,linewidth=4)    #line width is for long line goes according to value of axes
plt.title("SQUARE OF THE NUMBER",fontsize=27)  
plt.xlabel("Value",fontsize=15)
plt.ylabel("Square of the value",fontsize=15)
plt.tick_params(axis="both",labelsize=13)  #labelsize is used as it is used for axes's label font size
plt.show()

#plt.() no equal values
