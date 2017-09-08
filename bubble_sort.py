from RandList import MakeList

#ソートするリスト作成
li = MakeList()
print(li)

#ソート
n = len(li)
for i in range(n,0,-1):
    for j in range(i-1):
        if li[j] > li[j+1]:
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp

print(li)
