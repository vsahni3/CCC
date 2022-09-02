num = int(input())
max = num // 5
count = 0
seen = set()
for i in range(max+1):
    cur = i * 5
    rem = num - cur
    if rem % 4 == 0:
      
        seen.add((i, rem // 4))
        count += 1
    

max = num // 4
for i in range(max+1):
    cur = i * 4
    rem = num - cur
    if rem % 5 == 0:
   
        if (rem // 5, i) not in seen:
           
            count += 1
    

print(count)



# big = set()
# def recurse(n=0, cur=tuple()):
#     if n + 4 == num:
#         big.add(tuple(sorted(cur + (4,))))
#     elif n + 5 == num:
#         big.add(tuple(sorted(cur + (5,))))
#     else:
#         if n + 4 < num:
#             recurse(n+4, cur+(4,))
#         if n + 5 < num:
   
#          recurse(n+5, cur+ (5,))

# recurse()
# print(len(big))

