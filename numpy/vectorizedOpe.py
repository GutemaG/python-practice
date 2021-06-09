from __future__ import print_function
import numpy as np

nums=np.arange(5,dtype=int)
nums=nums*10
nums=np.sqrt(nums)
np.ceil(nums)#floor,rint
np.isnan(nums)# check for NaN
nums + np.arange(5)
np.maximum(nums,np.array([1,-2,3,-4,23]))# compare element

vec1=np.random.randn(10)
vec2=np.random.randn(10)
dist=np.sqrt(np.sum((vec1-vec2)**2))


v1=np.arange(5)
v2=np.arange(5,10)
d=np.sqrt(np.sum((v1-v2)**2))

rnd=np.random.randn(4,2)
'''
rnd.mean()
rnd.std()
rnd.argmin()
rnd.sum()
rnd.sum(axis=0)
rnd.sum(axis=1)
(rnd>0).sum()# counts nuber of positive values
(rnd>0).any()# check if any vlaue is True
(rnd>0).all() # checks if all values are True
'''

#Brodcast
a=np.array([[0,0,0],
            [10,10,10],
            [20,20,20],
            [30,30,30]
            ])
b=np.array([0,1,2])
#print(a+b)