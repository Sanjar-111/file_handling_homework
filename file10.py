def main(data:str):
    txt=open(data,"r")
    txt=txt.read()
    ls=txt.split("\n")
    count=0
    for i in ls:
        if count<len(i):
            count=len(i)
    return count
print(main("data/data10.txt"))


# Read data from file