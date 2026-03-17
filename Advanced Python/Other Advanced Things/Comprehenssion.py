l=[]
for i in range(10):
    if i%2==0:
        l.append(i)
print(l)

# Using List Comprehenssion , above code can be written as
L = [i for i in range(10) if i%2==0]
print(L)

M = [i**2 for i in range(10) if i%2==0]
print(M)

# Using Dictionary Comprehenssion
print("\nUsing Dictionary Comprehenssion:")
D = {i:i**2 for i in range(10) if i%2==0}
print(D)