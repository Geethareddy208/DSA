ans=[]
n=int(input())
def binary(n):
    if n==0:
        return
    binary(n//2)
    ans.append(n%2)
binary(n)
ans=ans[::-1]
counteven=0
countodd=0
for i in range(len(ans)):
    if ans[i]==1:
        if i%2==0:
            counteven+=1
        else:
            countodd+=1
print(counteven,countodd)

