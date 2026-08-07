
#right triangle number pattern
'''n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()'''


#inverted right triangle number pattern
'''n=5
for i in range(1,n+1):
    for j in range(n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()'''


#left triangle number pattern
'''n=5
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for j in range(n-i+1):
        print(j+1,end="")
    print()'''


#inverted left triangle number pattern
'''n=5
for i in range(1,n+1):
    for j in range(n-i+1):
        print(j+1,end="")
    print()'''


#inverted right triangle number pattern
'''n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print(j+1,end="")
    print()'''


#right triangle number pattern
'''n=5
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for j in range(2*n-(2*i-1)):
        print(j+1,end="")
    print()'''