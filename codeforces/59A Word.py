s = input()

count_lower = 0
for i in s:
    if i.islower():
        count_lower += 1
count_upper = len(s) - count_lower

if count_lower >= count_upper:
    output = [ i.lower() for i in s]
else:
    output = [ i.upper() for i in s]

print("".join(output))
