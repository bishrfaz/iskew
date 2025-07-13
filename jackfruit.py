n,d=map(int,input().split())

weight=list(map(int,input().split()))
weight.sort(reverse=True)

jam=0
jam+=sum(weight[:d])
print(jam)
    
