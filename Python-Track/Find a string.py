def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-2):
        if sub_string==string[i,i+1,i+2]:
            count+=1
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
