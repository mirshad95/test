
for _ in range(int(input())):
    n = int(input())
    l = input().split()[:n]
    c=0
    for i in l:
        if i=="cookie":
            c+=1
        else:
            c=0
            
        if c==2:
            break
    if c==0:
        print("YES")
    else: 
        print("NO")