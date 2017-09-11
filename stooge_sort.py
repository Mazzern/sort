from RandList import MakeList

#ソートするリスト作成
li = MakeList()
print(li)

#ソート
def StoogeSort(li, i=0, j=len(li)-1):
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

#実行
li = StoogeSort(li, i=0, j=len(li)-1)
print(li)
