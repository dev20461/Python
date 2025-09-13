# 1 0 1 0 1
# 1 0 1 0
# 1 0 1
# 1 0
# 1




n=5

for i in range(n,0,-1):
    for j in range(i):
        print(j%2,end=" ")
    print()    