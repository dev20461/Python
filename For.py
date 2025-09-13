

# Used when we already know how many times to repeat. Works with range() and collections (list, tuple, etc.).

i=10

for i in range(2,10,4):
    print(i),
    



# q2

for i in range(1,20):
    print(f"{i} squared = {i*i}")


# q4

for i  in range(1,31):
    if i%2 !=0:
        print("q4 op",i)



#q7

text="PYTHON"

for ch in text:
    if ch in "AEIOU":
        continue
    print(ch)
    