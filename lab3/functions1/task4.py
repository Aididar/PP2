lis=[2,3,4,5,6,7]
def filter(num):
    s=0
    for i in range(2,num):
        if num%i==0:
            s=s+1
    if s==0:
        print(num)

for i in range(6):
    filter(lis[i])
