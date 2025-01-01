nums = [2,7,11,15]
target = 9

map = {}
ans = []

for i,n in enumerate(nums):
    find = target - n

    if find in map:
        ans.append(map[find])
        ans.append(i)

    map[n] = i

print(ans)
