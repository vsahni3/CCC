# same = {}
# for i in range(int(input())):
#     cur = input()
#     if cur[2] not in same:
#         if cur[0] not in same:
#             same[cur[0]] = [cur[2]]
#         else:
#             same[cur[0]].append(cur[2])

# diff = {}
# for i in range(int(input())):
#     cur = input()
#     if cur[2] not in diff:
#         if cur[0] not in diff:
#             diff[cur[0]] = [cur[2]]
#         else:
#             diff[cur[0]].append(cur[2])

# count = 0
# for i in range(int(input())):
#     cur = input().split()
#     for i in cur:
#         if i in same:
#             for j in same[i]:
#                 if j not in cur:
#                     count += 1
#         if i in diff:
#             for j in diff[i]:
#                 if j in cur:
#                     count += 1
# print(count)

count = 0
first = set()
for i in range(int(input())):
    first.add(tuple(sorted(input().split())))
second = set()
for i in range(int(input())):

    second.add(tuple(sorted(input().split())))
third = set()
for i in range(int(input())):
    cur = input().split()
    third.add(tuple(sorted((cur[0], cur[1]))))
    third.add(tuple(sorted((cur[0], cur[2]))))
    third.add(tuple(sorted((cur[1], cur[2]))))

for i in first:
    if i not in third:
       
        count += 1
for i in second:
    if i in third:
        
        count += 1
print(count)

