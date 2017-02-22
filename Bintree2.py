from BintreeFile import Bintree

svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end=" ")
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

engelska = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engelskafil:
    for line in engelskafil:
        words = line.strip(' ')               # Ett trebokstavsord per rad
        word = words.split()
        for i in word:
            if i in engelska:
                pass
            else:
                engelska.put(i)
                if i in svenska:
                    print(i, end=" ")           # in i sökträdet
print("\n")