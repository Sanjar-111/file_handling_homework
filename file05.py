import string
def main(data:str):
    a=open(data,"r")
    n=a.read()
    i=0
    digit=string.digits
    count=0
    while len(n)>i:
        if n[i] in digit:
            count+=1
        i+=1
    return [count]+[len(n)-count]
print(main("data/data05.txt"))
