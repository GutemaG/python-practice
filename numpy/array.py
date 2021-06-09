from __future__ import print_function
import numpy as np

data1=[1,2,3,4,5]
arr1=np.array(data1)
data2=[range(1,5),range(5,9)]
arr2=np.array(data2)
arr2.tolist()
################

#Seclection
a03=arr[0,4]# == arr[0][3] it returns row 0 coloumn 3 element 
##sliciing of array
a1=arr[0,:]#row 0; return 1 d array 
a2=arr[:0]# column 0; 
a3=arr[:,:2]# columns strictly before index 2
a4=arr[:,2:]# column after index 2 incliuded
a5=arr[:,1:4]
reversarray=arr[0,::-1]



np.zeros(10)# print 1D 10 zeros
np.linspace(0,1,5)#  0 to 1 (inclusive) with 5 points
np.logspace(0,3,4) #10^0 to 10^3(inclusiv3 with 4 poings)


int_array=np.arange(5)
float_array=int_array.astype(float)

arr=np.arange(10,dtype=float).reshape((2,5)) ##reshapeing the dimenstion of an array

print(arr.shape)
#print(arr.reshape(5,2))

a=np.array([0,1])
a_col=a[:, np.newaxis]
#print(a_col)
#print(a_col.T)#print transpose of a_col

arr_flt=arr.flatten()# Flatten always return ta flat copy of the orriginal array
arr_flt[0]=33
#print(arr_flt)

arr_flt=arr.ravel()# ravel return a view of the original array whenever possible
arr_flt[0]=33
#print(arr_flt)
#print(arr)

###stackarrays

a=np.array([0,1])
b=np.array([2,3])
ab=np.stack((a,b)).T # ==np.hstack((a[:, None],b[:, None]))
#print(ab)

