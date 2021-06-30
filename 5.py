n=int(input())
s=0
p=1
while n>0 and n<100000:
    s=s+(n%10)
    p=p*(n%10)
    n=n//10
print(p-s)