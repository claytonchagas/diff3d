import numpy as np

f = open('/home/clayton/cuboasc.stl','r')
data = np.genfromtxt(f)
# delete(data,0,0) # Erases the first row (i.e. the header)
# plot(data[:,0],data[:,1],'o')
f.close()