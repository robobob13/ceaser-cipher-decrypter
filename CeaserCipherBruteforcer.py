## Taken from geeksforgeeks practically
def ceaserdecrypt(txt,s,fronts,rang):
    fin = ""
    x=""
    for i in range(len(txt)):
        x = txt[i]
        fin += chr((ord(x)+(rang-s)-fronts)%rang+fronts)
    return fin

#Tries every possible combination shifting ASCII/Unicode values of the characters. 
def ceaserdecryptbrute(message,fs,rngg):
    dictionary = {}
    for i in range(1,(rngg+1),1):
        msg = ceaserdecrypt(message,i,fs,rngg)
        dictionary.update({i:msg})

while True:
        msg = str(input("Encrypted MSG: "))
        if msg=="exit":
            print("Exiting")
            break
        ## Front shift in terms of ASCII/Unicode. 65 for capital letters, 97 for small, 33 for every commonly used character. 
        fs = int(input("Front Shift: "))
        ## Range. 26 for all letters, and more if you need. Just check a unicode cheat sheet im not writing this all down. 
        rngg = int(input("Range/Reps: "))
        brute = ceaserdecryptbrute(msg, fs, rngg)
        for shiftf, output in brute.items():
            print(f'{shiftf} : {output}')
        print("\n")