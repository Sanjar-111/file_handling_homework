import string
def main(data:str):
    a=open(data,"r")
    n=a.read()
    b=string.digits
    digit=0
    for i in n:
        j=0
        while len(b)>j:
            if b[j]==i:
                digit+=int(i)
            j+=1
    return digit
print(main("data/data07.txt"))