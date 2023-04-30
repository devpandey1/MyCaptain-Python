n=str(input("Enter a string"))
count={"i":0,"s":0,"p":0,"m":0}
for i in n:
    if i == "m":
        count['m']=count['m']+1
    elif i == "i":
        count['i']=count['i']+1
    elif i == "s":
        count['s']=count['s']+1
    elif i=="p":
        count['p']=count['p']+1

print("i = ",count['i'])
print("s = ",count['s'])
print("p = ",count['p'])
print("m = ",count['m'])