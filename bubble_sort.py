import time
import numpy as np

#ソート
def bubble_sort(li):
    n = len(li)
    for i in range(n,0,-1):
        for j in range(i-1):
            if li[j] > li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp
    return li

if __name__ == '__main__':
    Min = 1
    Max = 1000
    n = Max
    List = np.random.randint(Min, Max, n)

    st = time.time()

    srtli = bubble_sort(List)

    print(srtli)
    print(str(time.time() - st) + 'sec.')
