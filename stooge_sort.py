import time
import numpy as np

#ソート
def StoogeSort(li, i, j):
    if li[j] < li[i]:
        temp = li[i]
        li[i] = li[j]
        li[j] = temp
    if j-i+1 >= 3:
        t = (j-i+1)//3
        StoogeSort(li,i,j-t)
        StoogeSort(li,i+t,j)
        StoogeSort(li,i,j-t)
    return li

if __name__ == '__main__':
    Min = 1
    Max = 1000
    n = Max
    List = np.random.randint(Min, Max, n)

    st = time.time()

    srtli = StoogeSort(List, 0, len(List)-1)

    print(srtli)
    print(str(time.time() - st) + 'sec.')
