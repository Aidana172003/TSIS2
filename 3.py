line=input().split()
n=len(line)
counter=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if line[i]==line[j]:
            counter+=1
print(counter)