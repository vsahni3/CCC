n, c = [int(i) for i in input().split()]
points = [int(i) for i in input().split()]
seen = set()
def check(triple, length):
    return (abs(triple[0] - triple[1])) * (360 / length) + (abs(triple[1] - triple[2])) * (360 / length) >= 180
count = 0
print(check([1, 2, 3], 3))
for i in range(len(points)):
    for j in range(i, len(points)):
        for x in range(j, len(points)):
            if check((points[i], points[j], points[x]), c):
                if tuple(sorted((points[i], points[j], points[x]))) not in seen:
                    count += 1
                    seen.add(tuple(sorted((points[i], points[j], points[x]))))
print(count)
print(seen)


