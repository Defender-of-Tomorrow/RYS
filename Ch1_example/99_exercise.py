## 연습문제 5
#a = ['a','b','c','d','e','f','g','h','i','j']
#print(a[7:0:-1])

## 연습문제 9
#import numpy as np

#np.random.seed(10)
#a = np.random.randint(100, size=9)
#b = a.sum()
#c = a.mean()
#print('sum(a)=', b)

##d = 'mean(a)= {0:.2f}'.format(c)
##print(d)
#print('mean(a)=', c)

# 연습문제 10
import numpy as np

def Find_Xst_biggest(arr):
    nMax = 0

    for i in range(0, 50):
        if arr[i] >= nMax:
            nMax = arr[i]
            res = i
    arr[res] = 0
    return res, nMax

np.random.seed()
arr = np.random.randint(low=0, high=50, size=1000000000)
#print(arr)

count = np.bincount(arr)
print('count: ', count)


for i in range(0, 3):
    rank, rank_count = Find_Xst_biggest(count)
    print('rank', i + 1, ': ', rank, 'cnt: ', rank_count)
