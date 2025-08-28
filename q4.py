
# 1 0 1 0 1
#   0 1 0 1
#     1 0 1
#       0 1
#         1



    
n = 5

for row in range(n):                        
    print("  " * row, end="")               

    for col in range(n - row):            
        print((row + col) % 2, end=" ")     
    print()