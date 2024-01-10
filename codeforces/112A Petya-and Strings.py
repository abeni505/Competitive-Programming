
num1 = input()
num2 = input()

for i in range(len(num1)):
    if num1[i].lower() < num2[i].lower():
        print(-1)
        break
    elif num1[i].lower() > num2[i].lower():
        print(1)
        break
else:
    print(0)