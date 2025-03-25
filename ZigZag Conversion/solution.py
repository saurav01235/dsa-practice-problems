str1 = "PAYPALISHIRING"
row = 4

arr = [[], [], [], []]


for i in arr:
    r = row
    while r > 0:
        i.append("-")
        r -= 1

i = 0
while i < len(str1):
    j = 0
    while j < 4 and i<len(str1):
        arr[j].append(str1[i])
        j += 1
        i += 1
    j = 3
    while j >= 0 and i<len(str1):
        arr[j].append(str1[i])
        i += 1

for i in arr:
    for j in i:
        print(j, " ", end=" ")
    print("", )
