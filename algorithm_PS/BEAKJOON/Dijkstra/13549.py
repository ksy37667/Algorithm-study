from heapq import *
N,K=map(int,input().split())
Max=10**5+1
D=[-1]*Max
D[N]=0
q=[]
heappush(q,[0,N])
while q:
    t,x=heappop(q)
    for nx in [2*x,x+1,x-1]:
        if 0<=nx<Max and D[nx]==-1:
            if nx==x*2:
                heappush(q,[t,nx])
                D[nx]=t
            else:
                heappush(q,[t+1,nx])
                D[nx]=t+1
print(D[K])