import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(2,6,4)
simlen = int(1e6) 
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('half_gaussian.dat',dtype='float')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,4):
	err_ind = np.nonzero(randvar > x[i]) 
	err_n = np.size(err_ind) 
	err.append(err_n/simlen) 
	
plt.plot(x.T,err)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')


plt.show() 
