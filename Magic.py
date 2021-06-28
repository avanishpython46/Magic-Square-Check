def is_magic_square(c,r,d):
    l = []
    l1 = []
    l2 = []
    for i in range(0,len(c)-1):
        if (c[i] == c[i+1]):
            l.append(True)
        else:
            l.append(False)
    for x in range(0,len(r)-1):
        if (r[x] == r[x+1]):
            l1.append(True)
        else:
            l1.append(False)

    for y in range(0,len(d)-1):
        if (d[y] == d[y+1]):
            l2.append(True)
        else:
            l2.append(False)
    if (all(l) and all(l1) and all(l2)):
        return True
    else:
        return False
side = int(input())
dm = side
mat = [[] for i in range(1,side+1)]
for i in range(1,side+1):
    nums = input().split()
    for x in nums:
        x = int(x)
        mat[i-1].append(x)
#columns sum
all_columns_sum = []
all_rows_sum = []
all_diag_sum = []
for i in mat:
    all_columns_sum.append(sum(i))
#diagonal sum
v,sums = 0,0
for i in mat:
    if (v==3):
        v = 0
    sums+=i[v]
    v+=1
v1,sums1 = 2,0
for x in mat:
    if (v1==-1):
        break
    sums1+=x[v1]
    v1-=1
v1 = v1 + 2
if (side > 3):
    for y in mat:
        if (v1==3):
            break
        sums1+=y[v1]
        v1+=1
all_diag_sum.append(sums)
all_diag_sum.append(sums1)
#row sum
def sum_all(ind):
    global mat
    sum1 = 0
    for i in mat:
        sum1+=i[ind]
    return sum1
for i in range(0,3):
    s1 = sum_all(i)
    all_rows_sum.append(s1)
print(is_magic_square(all_columns_sum,all_rows_sum,all_diag_sum))
