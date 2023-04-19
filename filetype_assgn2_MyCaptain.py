s=input("Input file name")
ex=s.split(".")[-1]
if ex=="py":
    print("The extension of the file is: python")
elif ex=="java":
    print("The extension of the file is: java")
elif ex=="c":
    print("The extension of the file is: C")
else:
    print("I don't know the extension of file")