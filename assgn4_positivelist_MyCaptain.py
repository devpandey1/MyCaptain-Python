list1=[]
list2=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    element=int(input())
    list1.append(element)
for numbers in list1:
    if(numbers>0):
        print(numbers)
        list2.append(numbers)
print(list2)