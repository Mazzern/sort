import time
import numpy as np

#ソート
def selection_sort(li):
    n = len(li)
    for i in range(n):
        mini = i
        for j in range(i+1,n):
            if li[j] < li[mini]:
                mini = j
        temp = li[i]
        li[i] = li[mini]
        li[mini] = temp
    return li

if __name__ == '__main__':
    Min = 1
    Max = 1000
    n = Max
    List = np.random.randint(Min, Max, n)

    st = time.time()

    srtli = selection_sort(List)

    print(srtli)
    print(str(time.time() - st) + 'sec.')
