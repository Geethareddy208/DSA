
n=int(input())   
ans=[]
while(n!=0):
    k=n%10
    ans.append(k)
    n=n//10
sum=0
product=1
for i in range(len(ans)):
    sum=sum+ans[i]
    product=product*ans[i]
print(product-sum)
