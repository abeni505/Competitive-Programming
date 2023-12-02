n = int(input())
a = list(map(int, input().split()))

even = False
odd = False
for i in a:
    if i%2 == 0:
        even = True
    else:
        odd = True
if even and odd: # there is at least one even and one odd number in the list so the sum will be odd so the array should be updated lexigraphically
    a.sort()
print(*a)
