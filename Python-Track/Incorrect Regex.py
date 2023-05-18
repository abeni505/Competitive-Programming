# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T=int(input())

for i in range(T):
    S=input()
    
    try:
        re.compile(S)
        print("True")
    except:
        print("False")
