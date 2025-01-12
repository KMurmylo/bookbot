def count_words(text):
    return len(text.split())

def count_characters(text):
    text_lowered=text.lower()
    chars={'a','b','c','d','e','f','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    dictionary={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

    for char in text_lowered:
        if char in chars:
            dictionary[char]+=1
    
    return dictionary
def sort_on(key):
    return key[1]

def print_report(file,text):
    print(f"-----report for {file}-----")
    print(f"found {count_words(text)} words total ")
    print("Chars found:")
    dict=count_characters(text)
    sorted=[]
    for key in dict:
        sorted.append([key,dict[key]])
    sorted.sort(reverse=True,key=sort_on)
    for key in sorted:
        #print(key[0])
        print(f"The character {key[0]} appears {key[1]} times")
    print("----- End of report -----")
    

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report("books/frankenstein.txt",file_contents)
    

main()



