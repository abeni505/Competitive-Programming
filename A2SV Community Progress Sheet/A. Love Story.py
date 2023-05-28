t=int(input())
code="codeforces"
count=0
for i in range(t):
    s=input()
    for i in range(len(s)):
        if s[i]==code[i]:
            count+=1
    

    print(len(code)-count)
    count=0
   
    


