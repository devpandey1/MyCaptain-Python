a=0
b=1
c=a+b
print(a,end=" ")
print(b,end=" ")
while c<=144:
    print(c,end=" ")
    temp=b
    b=c
    a=temp
    c=a+b