n=int(input("enter the number"))
ans=[]
while(n!=0):
    k=n%10
    ans.append(k)
    n=n//10
sum=0
for i in range(len(ans)):
    if i==0 or i==len(ans)-1:
        sum+=ans[i]
    else:
        continue
print(sum)