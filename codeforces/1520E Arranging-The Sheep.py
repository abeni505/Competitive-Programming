t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    prefix = [0] 
    suffix = [0]
    

    count = 0
    for i in range(len(s)):
        if s[i] == "*":
            prefix.append(prefix[-1])
            count += 1
        else:
            prefix.append(prefix[-1] + count)

    count = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == "*":
            suffix.append(suffix[-1])
            count += 1
        else:
            suffix.append(suffix[-1] + count)
    prefix = prefix[1:]
    suffix= suffix[:-1]
    suffix = suffix[::-1]

    for i in range(len(prefix)):
        prefix[i] += suffix[i]
    
    print(min(prefix))
    