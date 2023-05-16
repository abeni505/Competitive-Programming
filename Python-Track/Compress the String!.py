# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

s=input()


s_new=itertools.groupby(s)

for key,group in s_new:
    print((len(list(group)),int(key)),end=" ")
