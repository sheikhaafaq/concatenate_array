import numpy as np 
m,n,p = map(int,input().split())
print(m , n , p)
arr1 = np.array([input().split() for i in range(m)])
arr2 = np.array([input().split() for i in range(n)])

print(numpy.concatenate(arr1,arr2),axis =0)