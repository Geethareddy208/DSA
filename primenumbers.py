n=int(input("enter your number:"))
c=0
for i in range(1,n):
    if n % i ==0:
        c+=1
if c==2:
    print("it is prime")
else:
    print("it is not prime")