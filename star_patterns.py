#horizontal star pattern
'''n=5
print("*"*n,end=" ")'''

#vertical star pattern
'''n=5
for i in range(n):
    print("*")'''

# right triangle star pattern
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()'''

# inverted right triangle star pattern
'''n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()'''

#square pattern
'''n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()'''

#hollow square pattern
'''n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''