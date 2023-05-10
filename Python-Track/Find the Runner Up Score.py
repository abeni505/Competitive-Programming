if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
   
newlist= list(set(arr))
newlist.sort()
print(newlist[-2])
