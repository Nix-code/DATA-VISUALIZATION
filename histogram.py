import matplotlib.pyplot as plt
population_ages=[1,1,1,2,23,4,5,5,5,11,22,11,13,23,23,34,34,35,33,6,7,112,113,70,84,66,120]
bin=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bin,histtype='bar',rwidth=0.9 )

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Histogram")
plt.show()
