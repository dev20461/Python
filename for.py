# Used when we already know how many times to repeat. Works with range() and collections (list, tuple, etc.).

i=100

for i in range(1,100,2):
    print(i),
    



# q2

for i in range(1,11):
    print(f"{i} squared = {i*i}")


# q4

for i  in range(1,21):
    if i%2 !=0:
        print(i)



#q7

text="PYTHON"

for ch in text:
    if ch in "AEIOU":
        continue
    print(ch)
    