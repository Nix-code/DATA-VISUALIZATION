import matplotlib.pyplot as plt
x=[1,3,5,2,9]
y=[5,2,7,6,2]
x1=[8,4,6,11,3]
x2=[3,9,7,2,5]
plt.bar(x,y,label="example",color='g')
plt.bar(x1,x2,label="example2")
plt.title("Graph 1 ")
plt.xlabel("Numbers" )
plt.ylabel("Height" )
plt.legend()
plt.show()
