from RandList import MakeList

#ソートするリスト作成
li = MakeList()

print(li)

#ソート
n = len(li)
for i in range(n):
    mini = i
    for j in range(i+1,n):
        if li[j] < li[mini]:
            mini = j
    temp = li[i]
    li[i] = li[mini]
    li[mini] = temp

print(li)
