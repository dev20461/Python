# 5 4 3 2 1
#   5 4 3 2
#     5 4 3
#       5 4
#         5



n = 5
for i in range(n):                        
    for space in range(i):                
        print(" ", end=" ")               
    for num in range(n, i, -1):            
        print(num, end=" ")
    print()                                 