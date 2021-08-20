# importing required modules
from itertools import product

# mapping the input
k, m=map(int,input().split())
def square(n):
    return int(n)**2
list1=[]
for i in range(k):
    list1.append(list(map(square,input().split()[1:])))
Max=0
for ele in product(*list1):
    Sum=sum(ele)%m
    if Sum>Max:
        Max = Sum
        
print(Max)
