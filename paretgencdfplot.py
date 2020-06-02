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

#Markov cutoff	
A_1=np.array([2,0.798/2])
A_2=np.array([3,0.798/3])
A_3=np.array([4,0.798/4])
A_4=np.array([5,0.798/5])


#cheybschev cutoff
B_1=np.array([2,1/1.4448])
B_2=np.array([3,1/4.8488])
B_3=np.array([4,1/10.2528])
B_4=np.array([5,1/17.6568])

#chernov bound(for t=0.0001)
C_1=np.array([2,0.99987])
C_2=np.array([3,0.99977])
C_3=np.array([4,0.99967])
C_4=np.array([5,0.99957])

len= 3

x_A12= np.zeros((2,len))
x_A23= np.zeros((2,len))
x_A34= np.zeros((2,len))
x_B12= np.zeros((2,len))
x_B23= np.zeros((2,len))
x_B34= np.zeros((2,len))
x_C12= np.zeros((2,len))
x_C23= np.zeros((2,len))
x_C34= np.zeros((2,len))


lam= np.linspace(0,1,len)
for i in range(len):
	m= A_2-A_1
	temp1= A_1 + lam[i]*m
	x_A12[:,i]= temp1.T	

for i in range(len):
	m= A_3-A_2
	temp1= A_2 + lam[i]*m
	x_A23[:,i]= temp1.T	

for i in range(len):
	m= A_4-A_3
	temp1= A_3 + lam[i]*m
	x_A34[:,i]= temp1.T		

for i in range(len):
	m= B_2-B_1
	temp1= B_1 + lam[i]*m
	x_B12[:,i]= temp1.T	

for i in range(len):
	m= B_3-B_2
	temp1= B_2 + lam[i]*m
	x_B23[:,i]= temp1.T	

for i in range(len):
	m= B_4-B_3
	temp1= B_3 + lam[i]*m
	x_B34[:,i]= temp1.T		
	
for i in range(len):
	m= C_2-C_1
	temp1= C_1 + lam[i]*m
	x_C12[:,i]= temp1.T	

for i in range(len):
	m= C_3-C_2
	temp1= C_2 + lam[i]*m
	x_C23[:,i]= temp1.T	

for i in range(len):
	m= C_4-C_3
	temp1= C_3 + lam[i]*m
	x_C34[:,i]= temp1.T		
		
	

plt.plot(x_A12[0,:], x_A12[1,:])
plt.plot(x_A23[0,:], x_A23[1,:])
plt.plot(x_A34[0,:], x_A34[1,:])
plt.plot(x_B12[0,:], x_B12[1,:])
plt.plot(x_B23[0,:], x_B23[1,:])
plt.plot(x_B34[0,:], x_B34[1,:])
plt.plot(x_C12[0,:], x_C12[1,:])
plt.plot(x_C23[0,:], x_C23[1,:])
plt.plot(x_C34[0,:], x_C34[1,:])




plt.plot(A_1[0], A_1[1], 'ro')
plt.text(A_1[0]*(1+0.03), A_1[1]*(1-0.1), 'A_1')
plt.plot(A_2[0],A_2[1], 'ro')
plt.text(A_2[0]*(1+0.03), A_2[1]*(1-0.1), 'A_2')	
plt.plot(A_3[0],A_3[1], 'ro')
plt.text(A_3[0]*(1+0.03), A_3[1]*(1-0.1), 'A_3')
plt.plot(A_4[0],A_4[1], 'ro')
plt.text(A_4[0]*(1+0.03), A_4[1]*(1-0.1), 'A_4')
plt.plot(B_1[0], B_1[1], 'ro')
plt.text(B_1[0]*(1+0.03), B_1[1]*(1-0.1), 'B_1')
plt.plot(B_2[0],B_2[1], 'ro')
plt.text(B_2[0]*(1+0.03), B_2[1]*(1-0.1), 'B_2')	
plt.plot(B_3[0],B_3[1], 'ro')
plt.text(B_3[0]*(1+0.03), B_3[1]*(1-0.1), 'B_3')
plt.plot(B_4[0],B_4[1], 'ro')
plt.text(B_4[0]*(1+0.03), B_4[1]*(1-0.1), 'A_4')
plt.plot(C_1[0], C_1[1], 'ro')
plt.text(C_1[0]*(1+0.03), C_1[1]*(1-0.1), 'C_1')
plt.plot(C_2[0],C_2[1], 'ro')
plt.text(C_2[0]*(1+0.03), C_2[1]*(1-0.1), 'C_2')	
plt.plot(C_3[0],C_3[1], 'ro')
plt.text(C_3[0]*(1+0.03), C_3[1]*(1-0.1), 'C_3')
plt.plot(C_4[0],C_4[1], 'ro')
plt.text(C_4[0]*(1+0.03), C_4[1]*(1-0.1), 'C_4')

plt.plot(x.T,err)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')


plt.show() 
