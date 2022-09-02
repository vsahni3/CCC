n, m, k = [int(i) for i in input().split()]
def check(seq):
    count = 0
    for i in range(len(seq)):
        cur = [seq[i]]
        count += 1
        
        for j in range(i+1, len(seq)):
            cur.append(seq[j])
        
            if len(cur) == len(set(cur)):
                count += 1
         

    return count

def recurse(count=0, cur=[]):
    if count == n:
        if check(cur) == k:
            return cur
        return False

    for i in range(1, m+1):
        res = recurse(count+1, cur+[i])
        if res:
    
            return res
if [n, m, k] == [0, 0, 0]:
    print(0)
else:
    res = recurse()
    if res:
        for i in res:
            print(i, end=' ')
    else:
        print(-1)
