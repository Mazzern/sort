import time
import numpy as np

def med3(x, y, z):
    if x < y:
        if y < z:
            return y
        elif z < x:
            return x
        else:
            return z
    else:
        if z < y:
            return y
        elif x < z:
            return x
        else:
            return z

def quicksort(li, left, right):
    if left < right:
        i = left
        j = right
        pivot = med3(li[i], li[i+(j-i)//2], li[j])
        while True:
            while li[i] < pivot:
                i += 1
            while pivot < li[j]:
                j -= 1
            if i >= j:
                break
            temp = li[i]
            li[i] = li[j]
            li[j] = temp

            i += 1
            j -= 1

        quicksort(li, left, i-1)
        quicksort(li, j+1, right)

    return li

if __name__ == '__main__':
    Min = 1
    Max = 1000
    n = Max
    List = np.random.randint(Min, Max, n)

    st = time.time()

    srtli = quicksort(List, 0, len(List)-1)

    print(srtli)
    print(str(time.time() - st) + 'sec.')
