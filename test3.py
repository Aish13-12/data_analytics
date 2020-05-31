import numpy as np
import random
len=1000000
arr=np.random.chisquare(2,len)
fp=open("chisquareinbuiltgen.dat","w+")
for i in range(len):
	fp.write("%d\r\n"%arr[i])
fp.close	

