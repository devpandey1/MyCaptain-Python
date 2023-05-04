def most_frequent():
    word=input("ENter a word: ")
    freq={}
    for char in word:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    print("Frequency of each alphabet is: ")
    for char in sorted(freq):
        print(char, freq[char])

most_frequent()