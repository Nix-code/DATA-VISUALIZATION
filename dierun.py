import pygal
from die import Die
di=Die()#single die

"""make multiple rolls"""
store=[]
for i in range(100):
    result=di.roll_me()
    store.append(result)

frequency=[]
"""analyze the result"""
for value in range(1,di.num_die+1):
    fre=store.count(value)
    frequency.append(fre)
    #visualization of the data
hist=pygal.Bar()
hist.title="Result of rolling the die"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist.y_title="Frequency of rolling die"
hist.add('D6',frequency )
hist.render_to_file('dierun.svg')
