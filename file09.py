import string
def main(data:str):
    a=open(data,"r")
    n=a.read()
    numbers=string.digits
    digit=9
    for i in n:
        if i in numbers:
            if digit>int(i):
                digit=int(i)
    return digit
print(main("data/data09.txt"))