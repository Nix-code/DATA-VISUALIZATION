from dies import Dies
die=Dies()
results=[]
for result in range(1000):
    result=die.finalroll()
    results.append(result)
counting=[]
for value in range(1,die.die_count+1):
    c=results.count(value)
    counting.append(c)
print(counting)
    
