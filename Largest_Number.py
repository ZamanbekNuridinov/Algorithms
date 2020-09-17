n=int(input())
a=[]

for i in range(n):
    l=input()
    a.append(l)

b=[]
max=a[0]
while len(a)>0:
    for i in range(len(a)):
        if a[i]>max:
            max=a[i]
    b.append(a[i])
    a.remove(a[i])

print(f"Max element in this list is: {max}")
print(f"Largest number of some digits is: {b}")
