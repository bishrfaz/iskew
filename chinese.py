n=int(input())
day=list(map(int,input().split()))
night=list(map(int,input().split()))
x=int(input())

overtime=0
total=[]

day.sort()
night.sort(reverse=True)

for i in range(n):
    total=day[i]+night[i]
    if total>x:
        overtime+=(total-x)*100
print(overtime)

