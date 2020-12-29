import numpy as np 
m,n,p = map(int,input().split())
arr1 = np.array([input().split() for i in range(m)])
arr2 = np.array([input().split() for i in range(n)])

print(np.concatenate(arr1,arr2),axis =0)
